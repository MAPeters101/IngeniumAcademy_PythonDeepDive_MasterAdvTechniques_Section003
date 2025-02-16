import socket
import time
import multiprocessing


def start_tcp_server():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    s.bind(('localhost', 443))

    # Listen for incoming connections (max 5 connections)
    s.listen(5)
    print("Server is listening...")

    # Establish a connection with the client
    c, addr = s.accept()
    print(f"Got connection from {addr}")

    while True:
        # Receive data from the client
        client_message = c.recv(1024).decode()
        if not client_message:
            break
        print(f'Received message: {client_message}')

        # Send a response to the client
        c.send(f'Received your message: {client_message}'.encode())

    c.close()


def start_tcp_client():
    # Give server a moment to start
    time.sleep(2)

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server on a specific address and port
    s.connect(('localhost', 443))

    for i in range(5):
        # Send a message tothe server
        s.send(f'Hello from client, message {i}'.encode())

        # Receive the server's response
        print(s.recv(1024).decode())
        time.sleep()

    s.close()

