
import socket
import os

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12347))

filename = input("Enter file path to send: ")

try:
    with open(filename, "rb") as file:
        client.sendall(os.path.basename(filename).encode())
        client.sendall(b"\n")

        while True:
            data = file.read(4096)
            if not data:
                break
            client.sendall(data)

    print("File sent successfully.")

except FileNotFoundError:
    print("Error: File not found.")

client.shutdown(socket.SHUT_WR)
client.close()
