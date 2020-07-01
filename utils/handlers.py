import socket
import json
import requests


def log_error(a, b):
    print(a, b)
    pass


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
            pass

    def send_embed(self, **kwargs):
        payload = json.dumps({'embeds': [kwargs]})
        self._send_to_webhook(payload)

    def send_message(self, message):
        payload = json.dumps({'content': message})
        self._send_to_webhook(payload)


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
            pass

    def _send_to_server(self, payload: dict):
        payload = json.dumps(payload)
        try:
            self.server.send(payload.encode('utf-8'))
            self.response = self.server.recv(2000).decode('unicode_escape')
            print("Sent", payload)
        except socket.error as error:
            log_error(error, self.server)
            pass
        return self.response

    def _kill(self):
        try:
            self.server.close()
        except socket.error as error:
            log_error(error, self.server)
            pass

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
