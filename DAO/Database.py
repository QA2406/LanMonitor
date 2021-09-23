import mysql.connector
from mysql.connector import Error

class Database:
    __host = "localhost"
    __user = "root"
    __password = ""
    __database = "LanMonitor"
    connection = None
    connected = False

    def __int__(self):
        self.__connect()
    def __connect(self):
        try:
            self.connection = mysql.connector.connect(self.__host,self.__database,self.__user,self.__password)
            if(self.connection.is_connected()):
                self.connected = True
                print("Connected Successfully !")
        except Error as e:
            print("Error while connecting to mysql", e)


test = Database()
