import socket
import os

def file_transfer_client():
    try:
        # 1. Create TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 2. Connect to server
        client_socket.connect(('127.0.0.1', 12345))

        # 3. Get filename
        filename = input("Enter the filename to send: ")

        # 4. Check if file exists BEFORE sending filename
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            client_socket.close()
            return

        # 5. Send filename
        client_socket.sendall(filename.encode())

        # 6. Send file data in chunks
        with open(filename, 'rb') as file:
            while True:
                chunk = file.read(1024)
                if not chunk:
                    break
                client_socket.sendall(chunk)

        print(f"File '{filename}' sent successfully.")

    except Exception as e:
        print("Error:", e)

    finally:
        client_socket.close()

if __name__ == '__main__':
    file_transfer_client()
