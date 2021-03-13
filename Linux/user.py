import os,signal,socket,threading,subprocess as sp

tmp = sp.call('clear',shell=True)
disconnect = False
shutdown = False


def recvdt():
    try:
        while True:
            data=t.recv(1024)
            if data.decode("utf-8") == "Connection Lost!":
                shutdown = True
                print("\rConnection lost...Press enter to exit!")
                break
            elif disconnect == True:
                t.shutdown(socket.SHUT_RDWR)
                break
            print("\r< "+data.decode("utf-8")+"         \n> ",end="")
    except:
        pass
        

# try:
t=socket.socket()
port=47121
ip="192.168.240.128"#+input("Enter ip 192.168.")
tmp = sp.call('clear',shell=True)
t.connect((ip,port))
t1=threading.Thread(target=recvdt,args=())
t1.start()
try:
    while True:
        chat=input("> ")
        if chat=="exit": 
            tmp = sp.call('clear',shell=True)
            t.sendall(bytes("Diconnected!","utf-8"))
            disconnect = True
            print("You are disconnected.")
            print(shutdown,disconnect)
            t.shutdown()
            break
        if shutdown == True:
            print("Shuting Down")
            t.shutdown(socket.SHUT_RDWR)
            break
        t.sendall(bytes(chat,"utf-8"))
except:
    print("")

t.close()
# except:
#     print("\033[FServer connection terminated!")
