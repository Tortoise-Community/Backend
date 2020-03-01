'''import socket
import json

#from settings import BOT_TOKEN

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
request = None



class DiscordHandler():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    




def send(id,value):
    package = {id:value} 
    payload = json.dumps(package)
    try:
        server.send(request.encode('utf8'))
        response = server.recv(255).decode('utf8')
        return response.get('status')
    except ConnectionAbortedError:
        print("aborted")

       

                 
def connection():
    try:
        server.connect(("34.68.150.139", 15555))
        send("Auth","test")
        resp = send("Send","test")
        print(resp)
    except ConnectionAbortedError:
        print("Connection closed by server.")






try:
    while request != 'quit':
        request_input = input('1 for auth, 2 for sending to text channel >> ')
        if request_input == "1":
            request = get_token_request()
        elif request_input == "2":
            request = get_send_channel_request()
        else:
            continue

        print("Sending to server .. ", end="")
        request = json.dumps(request)
        server.send(request.encode('utf8'))
        try:
            response = server.recv(255).decode('utf8')
        except ConnectionAbortedError:
            print("Connection closed by server.")
            break
        print("Server response:", response)
except KeyboardInterrupt:
    server.close()

'''   