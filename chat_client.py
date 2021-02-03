import socket

port = 8080

s=socket.socket()
pc_name = input("Server name eingeben: ")


s.connect((pc_name,port))
print("Verbunden mit Server")

while 1: 
    nachricht_empf=s.recv(1024)
    print(":: ", nachricht_empf.decode())

    nachricht= input(">>")
    s.send(nachricht.encode())