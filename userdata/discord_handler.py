import socket
from Tortoise.views import Members 
from . import models
from Tortoise.settings import Encryption_key

class Display():
    name  : str
    tag : int
    activity : str
    level : int
    high_role : str

s =  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip =  socket.gethostname()
port = 1328
s.bind((ip,port))
s.listen(5)



