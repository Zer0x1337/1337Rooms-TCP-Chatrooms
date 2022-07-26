import socket
import os
import sys
from sys import platform
from threading import Thread


if platform == "linux" or platform == "linux2":
        os.system('clear')
elif platform == "win32":
        os.system('cls')

print("""                                              
  __ ____ ____ ______ _____                            
 /_ |___ \___ \____  |  __ \                           
  | | __) |__) |  / /| |__) |___   ___  _ __ ___  ___  
  | ||__ <|__ <  / / |  _  // _ \ / _ \| '_ ` _ \/ __| 
  | |___) |__) |/ /  | | \ \ (_) | (_) | | | | | \__ \  
  |_|____/____//_/   |_|  \_\___/ \___/|_| |_| |_|___/ 
                                                       
""")

chatroom = int(input("Choose a 1337Room (1-10): ")) #room input
username = input("Choose a Username: ") #username input

if platform == "linux" or platform == "linux2":
        os.system('clear')
elif platform == "win32":
        os.system('cls')


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if chatroom == 1:
    client.connect(("127.0.0.1", 1337))
if chatroom == 2:
    client.connect(("127.0.0.1", 1337))
if chatroom == 3:
    client.connect(("127.0.0.1", 1337))
if chatroom == 4:
    client.connect(("127.0.0.1", 1337))
if chatroom == 5:
    client.connect(("127.0.0.1", 1337))
if chatroom == 6:
    client.connect(("127.0.0.1", 1337))
if chatroom == 7:
    client.connect(("127.0.0.1", 1337))
if chatroom == 8:
    client.connect(("127.0.0.1", 1337))
if chatroom == 9:
    client.connect(("127.0.0.1", 1337))
if chatroom == 10:
    client.connect(("127.0.0.1", 1337))

print(f"""------------------------------------------------------------------
  1337Room [#1]  |  UserName: {username}  |  ctrl+Z to exit...
------------------------------------------------------------------\n""")

def recieve():
    while True:
        try:
            msg = client.recv(1024).decode("ascii")
            if msg == "USER":
                client.send(username.encode("ascii"))
            else:
                print(msg)
        except Exception as e:
            print(e)
            print("error occured... wiping all drives.... lol")
            client.close()
            break

def send():
    while True:
        msg = f"{username}: {input()}"
        client.send(msg.encode("ascii"))

recieveing = Thread(target=recieve)
recieveing.start()

sending = Thread(target=send)
sending.start()