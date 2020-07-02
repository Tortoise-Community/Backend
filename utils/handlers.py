import socket
import logging

import json
import requests

from django.conf import settings

logger = logging.getLogger("Generic Logger")
logger.setLevel(level=logging.DEBUG)
formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
fileHandler = logging.FileHandler(filename="error.log")
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)


def log_error(exp, msg):
    logger.debug(f"{exp} raised on activity {msg}")


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


sock_hook = WebhookHandler(settings.WEBHOOK_ID,
                           settings.WEBHOOK_SECRET)


class SocketHandler:
    def __init__(self, socket_ip: str, port: int, token=None):
        self.socket_ip = socket_ip
        self.port = port
        self.token = token
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.response = None

    def _connect(self):
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
                                                            f"Payload: {payload}"}
            sock_hook.send_embed(data)
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
        resp = self._safe_packet_transfer(payload)
        print(resp["status"]["code"])

    def signal(self, sock_endpoint: str):
        payload = {"endpoint": "signal", "data": sock_endpoint}
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
