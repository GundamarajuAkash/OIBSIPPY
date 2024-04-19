import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'localhost'
port = 53
client.connect((host,port))

client_name = input("Enter your name:")
client.send(client_name.encode())

while True: 
    message = input(f"You:")

    client.send(message.encode())

    if message.lower() == "bye":
        break
        
    response = client.recv(1024).decode()
    print(f"Server{response}:")
    
client.close()