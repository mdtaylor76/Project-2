# Matt Taylor
# CST311 - Programming Assignment #1
# September 13th, 2020
# UDPClient.py - UDP Socket Client

from socket import *    
serverName = 'localhost'    # Server Name
serverPort = 12000          # Server Port
clientSocket = socket(AF_INET, SOCK_DGRAM)      # Setup socket
clientSocket.settimeout(1.0)

lostPacket = 0

print("PING - Client")
ping = 'Ping'
for x in range(1,11):

    pingMsg = ping + str(x)

    print("\nMesg sent: " + pingMsg)

    clientSocket.sendto(pingMsg.encode(), (serverName, serverPort)) # Connect to server, encode, and send
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)    # Recieve response from server
        print("Mesg rcvd: ", modifiedMessage.decode())
    except timeout:
        print('No Mesg rcvd')
        print("PING " + str(x) + " Request Timed out")
        lostPacket += 1
    
clientSocket.close()                # Close connection

print("\nLost Packets:      ", lostPacket)
