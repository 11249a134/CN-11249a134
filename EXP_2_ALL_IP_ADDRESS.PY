import socket

hostname = socket.gethostname()

print("Host Name:", hostname)
print("IP Addresses:")

ip_addresses = socket.getaddrinfo(hostname, None)

for address in ip_addresses:
    ip = address[4][0]
    print(ip)
