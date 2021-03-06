"""
UDP-Client.py
Paul Talaga
Feb 7, 2020
Desc: Lab 4 chat client.

"""
import socket

serverIP = 'localhost'
serverPort = 1200


if __name__ == "__main__":
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        message = input("Enter a message:")
        clientSocket.sendto(message.encode('utf-8'), (serverIP,serverPort))
        
        # Wait for a response
        (newMessage, serverAddress) = clientSocket.recvfrom(2048)
        
        print(newMessage.decode('utf-8'))
        
    clientSocket.close()
    
  