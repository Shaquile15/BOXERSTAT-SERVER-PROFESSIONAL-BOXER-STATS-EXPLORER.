import socket

def decrypt(text, shift=3):
    return ''.join(chr(ord(c) - shift) for c in text)

def handle_client(conn):
    authenticated = False

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        message = decrypt(data)

        if message.startswith("AUTH"):
            parts = message.split(",")
            username = parts[1]
            password = parts[2]

            if username == "admin" and password == "password":
                conn.send("Success: Authenticated".encode())
                authenticated = True
            else:
                conn.send("Error: Invalid credentials".encode())
                break

        elif message.startswith("BOXER") and authenticated:
            parts = message.split(",")
            name = parts[1]
            weight = parts[2]
            record = parts[3]

            print(f"Received boxer info - Name: {name}, Weight: {weight}, Record: {record}")
            conn.send(f"Received boxer: {name}".encode())
        else:
            conn.send("Error: Not authenticated or bad request".encode())

    conn.close()

# Server setup
server = socket.socket()
server.bind(('localhost', 9999))
server.listen(1)
print("Server is listening on port 9999...")

while True:
    conn, addr = server.accept()
    print(f"Connection from {addr}")
    handle_client(conn)
