import json
import socket
import logging

import requests

from django.conf import settings
from django.core.mail import send_mail


logger = logging.getLogger("Generic Logger")
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
fileHandler = logging.FileHandler(filename="error.log")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)


class WebhookHandler:

    headers = {'Content-Type': 'application/json'}
    resp = None

    def __init__(self, webhook_id, secret):
        self.webhook_id = webhook_id
        self.secret = secret
        self.url = "https://discordapp.com/api/webhooks/{}/{}".format(self.webhook_id, self.secret)

    def _send_to_webhook(self, payload):
        payload = json.dumps(payload)
        try:
            self.resp = requests.post(url=self.url, headers=self.headers, data=payload)
        except Exception as exp:
            log_error(exp, payload)

    def send_embed(self, payload: dict):
        payload = {"embeds": [payload]}
        self._send_to_webhook(payload)

    def send_message(self, message: str):
        payload = {"content": message}
        self._send_to_webhook(payload)


alert_hook = WebhookHandler(settings.WEBHOOK_ID,
                            settings.WEBHOOK_SECRET)


class SocketHandler:
    def __init__(self, socket_ip: str, port: int, token=None):
        self.socket_ip = socket_ip
        self.port = port
        self.token = token
        self.response = None

    def _connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.settimeout(8)
        try:
            self.server.connect((self.socket_ip, self.port))
        except socket.error as error:
            log_error(error, self.server)

    def _send_to_server(self, payload: dict):
        payload = json.dumps(payload)
        try:
            self.server.send(payload.encode('utf-8'))
            self.response = self.server.recv(2000).decode('unicode_escape')
        except Exception as exp:
            data = {"title": "Socket Error", "description": f"Error: {exp}\n"
                                                            f"Payload: {payload}",
                    "color": 0xff0000
                    }
            alert_hook.send_embed(data)
            log_error(exp, self.server)
        return self.response

    def _kill(self):
        try:
            self.server.close()
        except socket.error as error:
            log_error(error, self.server)

    def _auth(self):
        data = {"auth": self.token}
        self._send_to_server(data)

    def _safe_packet_transfer(self, packet: dict):
        self._connect()
        self._auth()
        status_resp = json.loads(self._send_to_server(packet))
        self._kill()
        return status_resp

    def verify(self, member_id: int):
        payload = {"endpoint": "verify", "data": member_id}
        self._safe_packet_transfer(payload)

    def signal(self, sock_endpoint: str):
        payload = {"endpoint": "signal_update", "data": sock_endpoint}
        self._safe_packet_transfer(payload)

    def dm_user(self, member_id: int, message: str):
        payload = {"endpoint": "send",
                   "data": {"user_id": member_id,
                            "message": message
                            }
                   }
        self._safe_packet_transfer(payload)

    def send_to_channel(self, channel_id: int, message: str):
        payload = {"endpoint": "send",
                   "data": {"user_id": channel_id,
                            "message": message
                            }
                   }
        self._safe_packet_transfer(payload)

    def send_contact_data(self, data: dict):
        payload = {"endpoint": "contact",
                   "data": data
                   }
        self._safe_packet_transfer(payload)


class EmailHandler:

    def __init__(self, recipient: str, name: str, subject: str, msg=None, pre=None):
        self.recipiant = recipient
        self.name = name
        self.subject = subject
        self.msg = msg
        self.pre = pre
        self.send_email()

    def _get_preformatted_message(self):
        if self.subject == "Appeal-Infraction":
            content = "Your infraction appeal is received\nOur staff will go through it soon.\nWe'll notify you here" \
                      " within 3 days with the updates so make sure you check your mail frequently"
        elif self.subject == 'Partnership':
            content = "Thank you for showing interest to partner up with our server.\nWe will look into the details" \
                      " and have one of our staff sent over. Hope you have read the partnering policies and terms."
        elif self.subject == "Sponsorship":
            content = "Thank you for showing your interest in sponsoring us, We'll review the details and contact " \
                      "you here to discuss the sponsorship terms and policies withing 2-3 days."
        elif self.subject == 'Report-User':
            content = "Thank you for reporting the user.\nNote that we take all reports seriously, The user could" \
                      " even be banned from the community if the graveness of the act demands him/her to be.\n" \
                      "So we won't be tolerating attempts to frame someone or fake reports." \
                      " Please don't indulge in such activites or you could face consequences."
        elif self.subject == 'Data-Deletion':
            content = "Greetings from the Tortoise Community. We are sorry to see you leave. Our staff will look" \
                      " into your data deletion request.\nYou will receive a confirmation email before the data" \
                      " is deleted permanently from our database.\nIf you'd like to come back to the server," \
                      " please use this link: https://discord.gg/6xsaVQN"
        elif self.subject == 'Issue-Report':
            content = "Thank you for taking the time to report the issue. Reports like yours makes the community" \
                      " better.\nWe'll look into it soon and resolve the issue."
        else:
            content = "Thank you for contacting us.\nWe will review the details submitted below and reach you here." \
                      " So make sure you check your emails frequently"

        formatted_msg = f"Hi {self.name}!\n\n{content}\n\nTeam Tortoise"

        return formatted_msg

    def send_email(self):
        if self.pre is True:
            self.msg = self._get_preformatted_message()
        try:
            send_mail(self.subject, self.msg, 'Tortoise Community <tortoisecommunity@gmail.com>',
                      ['{}'.format(self.recipiant)])
        except Exception as exp:
            embed = {"title": "Exception while sending email",
                     "description": f"Exception: {exp}\n\n"
                                    f"Recipient: {self.recipiant}"
                                    f"Subject: {self.subject}",
                     "color": 0xff0000
                     }
            alert_hook.send_embed(embed)


def log_error(exp, msg):
    logger.debug(f"{exp} raised on activity {msg}")
    embed = {"title": "API Error",
             "description": f"`{exp}`\n\n",
             "color": 0xff0000
             }
    alert_hook.send_embed(embed)
