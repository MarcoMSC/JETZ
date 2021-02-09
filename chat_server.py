import socket

port = 8080

s=socket.socket()
pc_name = socket.gethostname()
print("Server gestartet auf: ", pc_name)


s.bind(('', port))
s.listen(1)
print("Server wartet auf Anfrage...")

connection,address= s.accept()
print(address, " hat sich verbunden.")
connection.send(b"Hallo")

while 1: 
    nachricht_empf = connection.recv(1024)
    print(":: ", nachricht_empf.decode())

    nachricht = input(">>")
    connection.send(nachricht.encode())
