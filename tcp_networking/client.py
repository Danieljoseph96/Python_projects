import socket
#client ip and port 
client_ip="127.0.0.1"
client_port=12345

#create a socket
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#socket connected
client.connect((client_ip, client_port))

#send the data
data= client.recv(1024)
print(f"Recived data from server:{data.decode('utf-8')}")

#message to server
message="hello ,server! "
client.send(message.encode('utf-8'))

#Close the client socket
client.close()