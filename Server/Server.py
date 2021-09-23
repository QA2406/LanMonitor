from socket import socket
from threading import Thread
from uuid import getnode as get_mac
import os
import time
from PyQt5 import QtWidgets
from Model.ClientModel import Client
import socket

class Server(Thread):
    __host = "127.0.0.1"
    __port =  9876
    __pass = "nopass"
    server_socket = None
    socket = None
    servergui = None
    client = None
    list_client = []
    TableWidget = None

    def __init__(self,ServerGUI,_TableWidget):
        super(Server,self).__init__()
        self.servergui = ServerGUI
        self.TableWidget = _TableWidget
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_socket.bind((self.__host,self.__port))
        self.server_socket.listen()

    def run(self):
        print("Server starting ")
        while True:
            (clientConnected,clientAddress) = self.server_socket.accept()
            print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
            self.add_client(clientConnected)
            self.load_data()

    def send(self):


    def add_client(self,_socket):
        computerName = socket.gethostname()
        ipAddress = socket.gethostbyname(computerName)
        macAddress = get_mac().__str__()
        windowAccount = os.getlogin()
        group = "defalut"
        start = time.perf_counter()
        connectTime = self.server_socket.gettimeout()
        status = "Monitoring"

        client_obj = Client(computerName,ipAddress,macAddress,"Anh",windowAccount,group,connectTime,status)
        self.list_client.append(client_obj)

    def load_data(self):
        row = 0
        self.TableWidget.setRowCount(len(self.list_client))
        for client in self.list_client:
             self.TableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(client.get_computerName()))
             self.TableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(client.get_ipAddress()))
             self.TableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(client.get_macAddress()))
             self.TableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(client.get_remark()))
             self.TableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(client.get_windowsAccount()))
             self.TableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(client.get_group()))
             self.TableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(client.get_connectTime()))
             self.TableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(client.get_status()))
             row += 1




    

        




