import socket

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:

    cmd = input(">> ")

    client.sendall((cmd + "\n").encode())

    data = client.recv(1024).decode()
    print(data)

    if cmd.upper() == "QUIT":
        break

client.close()