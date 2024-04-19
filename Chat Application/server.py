import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'localhost'
port = 53
server.bind((host,port))

server.listen()

print("CHAT ROOM")

while True:
    
    client,address = server.accept()
    client_name = client.recv(1024).decode()
    print(f"Client {client_name} with address {address} has joined the chat")
    
    while True:
        data = client.recv(1024).decode()
        if not data:
            break

        print(f"Client {address}:{data}")
    
        message = input("You:")
        client.send(message.encode())
    
        if message.lower() == "bye":
            break
        
    client.close()
    
    if message.lower() == "bye":
        break    
    

server.close()