import socket
import json

SERVER_TOKEN = "tortoise_123_test"

# Connection
SERVER = "34.68.150.139"
PORT = 15555


def SocketSend(payload):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((SERVER, PORT))
    auth = {"auth":SERVER_TOKEN}
    auth = json.dumps(auth)
    server.send(auth.encode('utf-8'))
    payload = json.dumps(payload)
    server.send(payload.encode('utf-8'))
    try:
        response = server.recv(2000).decode('unicode_escape')

    except ConnectionAbortedError:
        print("Connection closed by server.")
    print("Server response:", response)
    server.close()

class BotSocket():
    pass