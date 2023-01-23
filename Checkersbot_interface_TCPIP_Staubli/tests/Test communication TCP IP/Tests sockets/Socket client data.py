'''client envoi en TCP IP plusieurs valeurs au serveur'''

import socket
import struct

# la valeur recu par le Staubli est en ASCII
# par exemple si on envoi : 4 le staubli recoit 52 (correspond en ASCII)

def client_program():
    host = '172.31.0.1'  ##socket.gethostname()
    port = 5000  # socket server port number

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
    client_socket.connect((host, port))  # connect to the server
        
    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        # 3 valeurs envoyés
        packer = struct.Struct("d d d")
        
        #envoi : (valeur choisie, 16, 12)
        data = packer.pack(*(float(message), float(16),float(12)))
        client_socket.sendall(data)

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
    
    
    
    