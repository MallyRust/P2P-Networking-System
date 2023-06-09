# P2P-Networking-System
Final Project

This code allows users to send files to specific recipients, visualize supported file types (images, CSV, and JSON), and broadcast files to multiple clients connected to the server.

Let's go through the code in more detail:

1. The code starts by importing the necessary modules: `socket`, `os`, `PIL` from the Pillow library for image visualization, `csv` for CSV file handling, `json` for JSON file handling, and `time` for measuring latency.

2. It defines the server address (`SERVER_ADDRESS`) and port number (`SERVER_PORT`) to establish a TCP connection with the server.

3. The TCP socket (`client_socket`) is created to communicate with the server using the `socket.socket()` function. It then connects to the server using the `connect()` method.

4. The `send_file()` function is defined to handle the process of sending a file to another client. It prompts the user to enter the recipient client ID and the file path. If the file doesn't exist, it displays an error message and returns. Otherwise, it sends the recipient ID and file name to the server and calls the `send_data()` function to send the file data to the server.

5. The `send_data()` function is a helper function that handles sending both files and other data to the server. If the input (`data`) is a file path, it reads the file, gets the file size, sends the file size to the server, waits for acknowledgment, sends the file data to the server, waits for acknowledgment, and calculates the end-to-end latency. If the input is not a file path, it converts the data to JSON format, gets the data size, sends the data size to the server, waits for acknowledgment, sends the data to the server, waits for acknowledgment, and calculates the end-to-end latency.

6. The `visualize_file()` function is defined to handle file visualization. It prompts the user to enter the file path. If the file doesn't exist, it displays an error message and returns. It determines the file type based on the file extension. If it's an image file (JPG, JPEG, PNG, GIF), it uses the `Image.open()` function from the Pillow library to open and display the image. If it's a CSV file, it calls the `display_csv_data()` function to display the data. If it's a JSON file, it reads the JSON data, converts it to a Python object, and calls the `visualize_json_data()` function to display the data.

7. The `display_csv_data()` function handles displaying data from a CSV file. It reads the CSV file, converts the CSV data to a list of lists, and provides options to display the entire file or select data based on a specified date. It then iterates over the data and prints the selected rows or displays a message if the data is not found.

8. The `visualize_json_data()` function handles the visualization of JSON data. It takes the JSON data as input and checks if it's a list or a single object. If it's a list, it displays the available IDs and provides options to display the entire JSON data or select data based on the ID. If it's a single object, it simply displays the JSON data.

9. The `broadcast_file()` function is defined to handle broadcasting a file to multiple clients. It prompts the user to enter the file path. If the file doesn't exist, it displays an error message and returns. It sends a broadcast command to the server, sends the file name to the server, and calls the `send_data()` function to send the
