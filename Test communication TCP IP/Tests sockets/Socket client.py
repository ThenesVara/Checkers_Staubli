import socket
import time

def client_program():
    host = '172.31.0.1'  #'192.168.200.254' #socket.gethostname()  # as both code is running on same pc
    print(host)
    port = 5000  # socket server port number
    print("etape 1")
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print(client_socket)
    print("etape 2")
    '''
    while client_socket.connect((host,port)) is not True:
        print(".")
        time.sleep(1)'''
        
    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()