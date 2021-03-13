import time
import socket
import threading
import subprocess as sp

tmp = sp.call('clear',shell=True)
disconnect = False

def exitp():

    x=input()
    if x=="exit":
        tmp = sp.call('clear',shell=True)
        print("Server Terminated!")
        c1.sendall(bytes("Connection Lost!","utf-8"))
        c2.sendall(bytes("Connection Lost!","utf-8"))
        disconnect = True
        s.shutdown(socket.SHUT_RDWR)



def user1(c1,c2):
    try:
        while True:
            if disconnect:
                raise Exception()
            data1=c1.recv(1024)
            if data1.decode("utf-8")=="Diconnected!":
                c2.sendall(bytes("\rUser leave the conversation! ","utf-8"))
            else:
                c2.sendall(data1) 
            print("user 1: "+data1.decode("utf-8"))
    except:
        print("Disconnecting User1...",end='')
        time.sleep(1)
        print("OK")

def user2(c1,c2):
    try:
        while True:
            if disconnect:
                raise Exception()
            data2=c2.recv(1024)
            if data2.decode("utf-8")=="Diconnected!":
                c1.sendall(bytes("\rUser leave the conversation! ","utf-8"))
            else:
                c1.sendall(data2)
            print("user 2: "+data2.decode("utf-8"))
    except:
        print("Disconnecting User2...",end='')
        time.sleep(1)
        print("OK")

try:        
    s=socket.socket()
    port=47121
    ip="192.168.240.128"#+input("Enter ip 192.168.")
    tmp = sp.call('clear',shell=True)
    s.bind((ip,port))
    s.listen(1)
    print("Server started and listening! [Server IP: "+ip+"]")
    t0 = threading.Thread(target=exitp, args=())
    t0.start()
    c1,addr1=s.accept()
    print("User :",addr1,"connected!")
    c2,addr2=s.accept()
    print("User :",addr2,"connected!")

    c1.sendall(bytes("\r###### Welcome to server both users connected! ######\n//---------->write exit to leave the chat<----------//","utf-8"))
    t1 = threading.Thread(target=user1, args=(c1,c2))
    t1.start()

    c2.sendall(bytes("\r###### Welcome to server both users connected! ######\n//---------->write exit to leave the chat<----------//","utf-8"))
    t2 = threading.Thread(target=user2, args=(c1,c2))
    t2.start()

    s.close()
except:
    print("Unexpected Error occurred!")
