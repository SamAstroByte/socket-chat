import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            print("\nOther:", msg)
        except:
            break

def send():
    while True:
        msg = input()
        client.send(msg.encode())

threading.Thread(target=receive).start()
send()
