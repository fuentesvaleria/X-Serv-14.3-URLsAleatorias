#!/usr/bin/python3

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

mySocket.bind((socket.gethostbyname('localhost'), 1234))

mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2084))
        print('Answering back...')
        aleat= random.randint(1,1000)
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                        '<html><title>URLs Aleatorias</title>' +
						'</body>hola. ' +
						 '<a href= "http://localhost:1234/' +
						str(aleat) + 
                        '">Dame otra</a>' +
                        "</body></html>" +
                        '\r\n', 'utf-8'))
        recvSocket.close()
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()