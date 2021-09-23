import pickle
from threading import Thread
from socket import socket
from zlib import compress
from mss import mss
from Model.Request import Request

class ServerThread(Thread):
    server = None
    socket = None
    inStream = None
    outStream = None
    id = -1

    def __init__(self,_server,_socket,_id):
        self.socket = _socket
        self.server = _server
        self.id = _id

    def close(self):
        if self.socket != None:
            self.socket = None
        if self.inStream != None:
            self.inStream = None
        if self.outStream != None:
            self.outStream = None

    def get_id(self):
        return self.id
    
            
    



