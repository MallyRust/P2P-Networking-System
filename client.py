import socket
import os

import csv
import json

# Server address and port number
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 8000

# Create TCP socket for communication with the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Function to send a file to another client
def send_file():
    # Prompt the user to enter the recipient client ID
    recipient_id = input("Enter the recipient client ID: ")
    client_socket.send(recipient_id.encode())

    # Prompt the user to enter the file path
    file_path = input("Enter the file path: ")

    # Check if the file exists
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return

    # Send the file name to the server
    file_name = os.path.basename(file_path)
    client_socket.send(file_name.encode())

    # Send the file data to the server
    with open(file_path, 'rb') as file:
        data = file.read()
        client_socket.sendall(data)

    print("File sent successfully.")

# Function to visualize a file
def visualize_file():
    # Prompt the user to enter the file path
    file_path = input("Enter the file path: ")

    # Check if the file exists
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return

    # Determine the file type
    file_extension = os.path.splitext(file_path)[1]

    # Visualize image file
    if file_extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        try:
            image = Image.open(file_path)
            image.show()
        except Exception as e:
            print("Error opening the image:", str(e))
    # Visualize CSV file
    elif file_extension.lower() == '.csv':
        display_csv_data(file_path)
    # Visualize JSON file
    elif file_extension.lower() == '.json':
        try:
            with open(file_path, 'r') as file:
                json_data = json.load(file)
                visualize_json_data(json_data)
        except Exception as e:
            print("Error reading the JSON file:", str(e))
    else:
        print("Unsupported file type.")

# Function to display data from a CSV file based on date
def display_csv_data(file_path):
    try:
        with open(file_path, 'r') as file:
            csv_data = csv.reader(file)
            data = list(csv_data)  # Convert the CSV data to a list of lists

            # Display the entire CSV file or select data based on date
            display_choice = input("Enter 'all' to display the entire file or 'date' to select data by date: ")
            if display_choice.lower() == 'all':
                for row in data:
                    print(row)
            elif display_choice.lower() == 'date':
                selected_date = input("Enter the date to display (from 2020.01 to 2022.04): ")
                found_data = False
                for row in data:
                    if row[0] == selected_date:
                        print(row)
                        found_data = True
                if not found_data:
                    print("Data for the specified date not found.")
            else:
                print("Invalid choice.")
    except Exception as e:
        print(".")

# Function to visualize JSON data
def visualize_json_data(json_data):
    if isinstance(json_data, list):
        print("Available IDs:")
        for item in json_data:
            print(item['id'])
        selected_option = input("Enter 'all' to display the entire JSON data or 'id' to select data by ID: ")
        if selected_option.lower() == 'all':
            print(json.dumps(json_data, indent=4))
        elif selected_option.lower() == 'id':
            selected_id = input("Enter the ID to display: ")
            found_data = False
            for item in json_data:
                if item['id'] == selected_id:
                    print(json.dumps(item, indent=4))
                    found_data = True
            if not found_data:
                print("ID not found.")
        else:
            print("Invalid option.")
    else:
        print(json_data)

def broadcast_file():
    # Prompt the user to enter the file path
    file_path = input("Enter the file path: ")

    # Check if the file exists
    if not os.path.isfile(file_path):
        print("File does not exist.")
        return

    # Send the broadcast command to the server
    client_socket.send(b"BROADCAST")

    # Send the file name to the server
    file_name = os.path.basename(file_path)
    client_socket.send(file_name.encode())

    # Send the file data to the server
    with open(file_path, 'rb') as file:
        data = file.read()
        client_socket.sendall(data)

    print("File broadcasted successfully.")

# Main loop
while True:
    print("\nMenu")
    print("1. Send a file")
    print("2. Visualize a file")
    print("3. Broadcast a file")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        send_file()
    elif choice == '2':
        visualize_file()
    elif choice == '3':
        broadcast_file()
    elif choice == '4':
        break
    else:
        print("Invalid choice.")

# Close the client socket
client_socket.close()
