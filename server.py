import socket

HOST = "127.0.0.1"
PORT = 12345

dic = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server pornit...")

conn, addr = server.accept()
print("Client conectat:", addr)

while True:
    data = conn.recv(1024).decode().strip()

    if not data:
        break

    parts = data.split()
    cmd = parts[0].upper()

    try:

        if cmd == "ADD":
            key = parts[1]
            value = parts[2]
            dic[key] = value
            conn.sendall(b"OK - record add\n")

        elif cmd == "GET":
            key = parts[1]
            if key in dic:
                conn.sendall(f"DATA {dic[key]}\n".encode())
            else:
                conn.sendall(b"ERROR invalid key\n")

        elif cmd == "REMOVE":
            key = parts[1]
            if key in dic:
                del dic[key]
                conn.sendall(b"OK value deleted\n")
            else:
                conn.sendall(b"ERROR invalid key\n")

        elif cmd == "LIST":
            if len(dic) == 0:
                conn.sendall(b"DATA|\n")
            else:
                items = ",".join(f"{k}={v}" for k, v in dic.items())
                conn.sendall(f"DATA|{items}\n".encode())

        elif cmd == "COUNT":
            conn.sendall(f"DATA {len(dic)}\n".encode())

        elif cmd == "CLEAR":
            dic.clear()
            conn.sendall(b"all data deleted\n")

        elif cmd == "UPDATE":
            key = parts[1]
            value = parts[2]

            if key in dic:
                dic[key] = value
                conn.sendall(b"Data updated\n")
            else:
                conn.sendall(b"ERROR invalid key\n")

        elif cmd == "POP":
            key = parts[1]

            if key in dic:
                value = dic.pop(key)
                conn.sendall(f"DATA {value}\n".encode())
            else:
                conn.sendall(b"ERROR invalid key\n")

        elif cmd == "QUIT":
            conn.sendall(b"Connection closed\n")
            break

        else:
            conn.sendall(b"ERROR unknown command\n")

    except:
        conn.sendall(b"ERROR invalid command format\n")

conn.close()
server.close()