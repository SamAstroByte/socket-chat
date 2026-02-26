import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

clients = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr}")
    clients.append(conn)

    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                break

            print(f"{addr}: {msg}")

            # broadcast to others
            for c in clients:
                if c != conn:
                    c.send(msg.encode())

        except:
            break

    clients.remove(conn)
    conn.close()
    print(f"[DISCONNECTED] {addr}")

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[LISTENING] Server running on port {PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

start()
