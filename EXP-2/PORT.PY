import socket
target = input("Enter IP Address: ")
for port in range(1, 101):
    s = socket.socket()
    result = s.connect_ex((target, port))
if result == 0:
    print("Port", port, "is Open")
s.close()
