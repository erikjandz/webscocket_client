import socket

# Some global variables
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "86.95.5.74"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print("[CONNECTED] connected to server...")


def writeFile(content):
    f = open("client.txt", "w")
    f.write(content)
    f.close()


def handle_server():
    while True:
        message = client.recv(2048).decode(FORMAT)
        writeFile(message)
        print("[FILE UPDATED] client.txt got updated.")


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print("[MESSAGE SENT] message sent to server.")


send("Connected")
writeFile(client.recv(2048).decode(FORMAT))

handle_server()

# send(DISCONNECT_MESSAGE)
