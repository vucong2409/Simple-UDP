import time
import socket 

HOST = "localhost"
PORT = 12000
#Set timeout to 2 seconds
TIMEOUT = 2

#Set received file to 4096
BUF_SIZE = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

successCase = 10

rtt = []

for i in range(0,10):
    print("Ping",i, end="")
    message = "a"
    try:
        sendTime = time.time()
        s.sendto(message.encode('utf-8'), (HOST, PORT))
        s.settimeout(TIMEOUT)

        data, address = s.recvfrom(BUF_SIZE)
        getTime = time.time()        

        rtt.append(getTime - sendTime)

        print(" recv:", data.decode('utf-8'),"{:.5f}".format(getTime - sendTime) + "s")
    except socket.timeout:
        print (" timeout")
        successCase = successCase - 1

rttSum = 0
for i in rtt:
    rttSum = rttSum + i

print("Send 10 | Success", successCase, "| Rate:", successCase/10, "| RTT AVG:", "{:.5f}".format(rttSum/successCase) + "s")