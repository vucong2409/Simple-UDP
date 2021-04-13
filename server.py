#UDPPingerServer.py
#We will need the following module generate randomized lost packets 

import random
from socket import *

#Create an UDP socket
#Notice the use of SOCK_DGRAM for UDP packets
HOST = "localhost"
PORT = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((HOST, PORT))

while True:
    #Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    #Receive the client packet along with the address it is coming from 
    message, address = serverSocket.recvfrom(1024)
    #Capitalize the messsage from the client
    message = message.upper()
    #If rand < 4, we consider the packet lost and do not respond 
    if rand < 4:
        continue
    #Otherwise, the server respond
    serverSocket.sendto(message, address)
