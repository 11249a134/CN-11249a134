
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12347))
server.listen(1)

print("File Server is waiting for connection...")

conn, addr = server.accept()
print("Connected to:", addr)

filename = conn.recv(1024).decode()
print("Receiving file:", filename)

with open("received_" + filename, "wb") as file:
    while True:
        data = conn.recv(4096)
        if not data:
            break
        file.write(data)

print("File received successfully.")

conn.close()
server.close()
