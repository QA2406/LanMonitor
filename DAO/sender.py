from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient('192.168.38.1',9999)

th = threading.Thread(target=sender.start_stream())
th.start()

while input("") != 'stop':
    continue

sender.stop_stream()