
import socket


hostname = socket.gethostname()


ip_address = socket.gethostbyname(hostname)

print("Host Name:", hostname)
print("IP Address:", ip_address)
