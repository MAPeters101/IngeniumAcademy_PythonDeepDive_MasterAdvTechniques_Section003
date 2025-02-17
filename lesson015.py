import socket
import time
import multiprocessing


def start_udp_server():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    s.bind(('localhost', 443))
    print('UDP Server is listening...')

    while True:
        # Receive data and address from any client
        client_message, addr = s.recvfrom(1024)
        print(f"Received message from {addr}: {client_message.decode()}")

        # Send a response to the client
        s.sendto(f'Received your message: {client_message.decode()}'.encode(), addr)

def start_udp_client():
    # Give server a moment to start
    time.sleep(2)

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 443)

    for i in range(5):
        # Send a message to the server
        s.sendto(f'Hello from client, message {i}'.encode(), server_address)

        # Receive the server's response
        response, _ = s.recvfrom(1024)
        print(response.decode())
        time.sleep(2)

    # Close the connection (optional for UDP)
    s.close()


if __name__ == '__main__':
    server_process = multiprocessing.Process(target=start_udp_server)
    client_process = multiprocessing.Process(target=start_udp_client)

    server_process.start()
    client_process.start()







