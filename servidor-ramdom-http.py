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
                        #b"<p>And in particular hello to you, " +
				#debuelve una tupla con el puerto del otro lado address..
						'</body>hola. ' +
						 '<a href= "http://localhost:1234/' +
						str(siguiente_url) + 
                        '">Dame otra</a>' +
			#b"<img src='http://2.bp.blogspot.com/_63jCiXixFMk/R8xviDmjAII/AAAAAAAAAGQ/vgU_rFcyVO0/S1600-R/gsyc.jpg' alt='gsyc'>"
                        "</body></html>" +
                        '\r\n', 'utf-8'))
        recvSocket.close()
#en cualquiermomento que le de cotnral c me saldra esta interrupcion 
except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
