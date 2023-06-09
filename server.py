import socket
import os

# Server IP address and port number
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 8000

# Create TCP socket for server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))
server_socket.listen(25)

print("Server is running. Listening for connections...")

while True:
    # Accept client connection
    client_socket, client_address = server_socket.accept()
    print("Connection established with:", client_address)

    # Receive the recipient client ID
    recipient_id = client_socket.recv(1024).decode()

    # Receive the file name
    file_name = client_socket.recv(1024).decode()

    # Receive the file data
    data = b""
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        data += chunk

    # Save the received file to the recipient client
    file_path = os.path.join(recipient_id, file_name)
    os.makedirs(recipient_id, exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(data)

    print("File received for client:", recipient_id)

    # Close the client socket
    client_socket.close()