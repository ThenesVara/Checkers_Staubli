'''client envoi en TCP IP plusieurs valeurs au serveur'''

import socket
import time

def client_program():
    host = '172.31.0.1'  #socket.gethostname()  
    port = 5000  # socket server port number

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
    client_socket.connect((host, port))  # connect to the server

    '''
    while client_socket.connect((host,port)) is not True:
        print(".")
        time.sleep(1)'''
        
    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send 1 message
        
        #message from server
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # message suivant

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
