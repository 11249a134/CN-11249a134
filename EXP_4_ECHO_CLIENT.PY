
import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the echo server
client_socket.connect(("127.0.0.1", 12345))

print("Connected to Echo Server.")

while True:
    message = input("Enter message (type 'exit' to quit): ")

    if message.lower() == "exit":
        break

    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)
    print("Echo from Server:", data.decode())

client_socket.close()
print("Client closed.")
