import socket
#define ip and port 
host ="127.0.0.1" #localhost ownsystem
port=12345
#create a socket object
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket and ip and port
server.bind((host,port))
#listen for incomming connection max[listen](number)
server.listen(2)

print(f"Server is listen on {host}:{port}")

while True:
    #Accept the connection from client
    client_socket,client_address = server.accept()
    #Accept the connection from cliend
    print(f"Client is conneccted on {client_address} :{client_socket}")

    message = f"hello client i am server ip:{host}:{port}"
    client_socket.send(message.encode())

    data=client_socket.recv(1024)
    print(f"Recived data from  client:{data.decode('utf8')} ")

    client_socket.close()