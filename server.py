import socket
import os
import sys
from sys import platform
from threading import Thread


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 1337)) #address
server.listen()

clients = []
usernames = []

def broadcast(msg):
    for client in clients:
        client.send(msg) 

def handle(client):
    while True:
        msg = client.recv(1024)
        broadcast(msg)

def receive():
    while True:
        client, address = server.accept()
        print("Connected from {}".format(str(address)))

        client.send("USER".encode("ascii"))
        username = client.recv(1024).decode("ascii")
        usernames.append(username)
        clients.append(client)

        print(f"{username} Connected!")
        broadcast(f"{username} Connected!".encode("ascii"))
        #client.send("test!".encode("ascii"))

        thread = Thread(target=handle, args=(client,))
        thread.start()

if __name__ == "__main__":
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

    print("Checking for new connections....")
    receive()