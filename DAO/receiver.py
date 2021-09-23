from vidstream import StreamingServer,ScreenShareClient
import threading

receiver = StreamingServer('192.168.1.13',9999,)

th = threading.Thread(target=receiver.start_server())
th.start()

while input("") != 'stop':
    continue

receiver.start_server()

