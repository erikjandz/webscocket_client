import socket
import threading

# Some global variables
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.99.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def writeFile(content):
    f = open("client.txt", "w")
    f.write(content)
    f.close()


def handle_server():
    while True:
        message = client.recv(2048).decode(FORMAT)
        writeFile(message)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    writeFile(client.recv(2048).decode(FORMAT))


send("Hello World!")

# start a thread to listen to the server and update the client.txt
thread = threading.Thread(target=handle_server)
thread.start()

# send(DISCONNECT_MESSAGE)
