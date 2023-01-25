import checkers
import gamebot
from time import sleep
import pygame
import numpy as np
import sys
import socket
import struct

##COLORS##
#          R    G    B
WHITE = (255, 255, 255)
BLUE = (0,   0, 255)
RED = (255,   0,   0)
BLACK = (0,   0,   0)
GOLD = (255, 215,   0)
HIGH = (160, 190, 255)

##DIRECTIONS##
NORTHWEST = "northwest"
NORTHEAST = "northeast"
SOUTHWEST = "southwest"
SOUTHEAST = "southeast"

# mode 0 : Humain VS IA
# mode 1 : IA VS IA
# mode 5 ----> Interface choix mode
global mode 
mode = 5

global C
p=99
C = np.array([[p, 28, p, 29, p, 30, p, 31],[24, p,25 , p, 26, p, 27, p],[p, 20, p, 21, p, 22, p, 23],[16, p, 17, p, 18, p, 19, p],[p,12, p, 13, p, 14, p, 15],[8, p, 9, p, 10, p, 11, p],[p, 4, p, 5, p, 6, p, 7],[0, p, 1, p, 2, p, 3, p]])

 ###################################   COMMUNICATION TCP/IP - SOCKET   #################################
''' Envoi les positions des pions de l'interface à l'adresse IP du staubli'''
def client_program_init(): 
    global client_socket 
    host = '172.31.0.1'  ##socket.gethostname()
    port = 5000  # socket server port number
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
    client_socket.connect((host, port))  # connect to the server   
    return client_socket

def client_program(client_socket, pos):  

    message = pos[0]  # take input
    message2 = pos[1]  # take input
    message3 = pos[2]  # take input

    # si message3 = 0 -> mange rien
    packer = struct.Struct("d d d")
        
    #envoi : (valeur choisie, valeur choisie2, valeur choisie3)
    data = packer.pack(*(float(message), float(message2),float(message3)))
    client_socket.sendall(data)

    #client_socket.close()  # close the connection




def interface(mode): 
    global compteur
    compteur = 0
    
    ################   PARAMETRES INTERFACE   ###################
    # initializing the constructor
    pygame.init()
    
    # screen resolution
    res = (720,720)
    
    # opens up a window
    screen = pygame.display.set_mode(res)
    
    # white color and light shade of the button and dark shade of the button
    color = (255,255,255)
    color_light = (170,170,170)
    color_dark = (100,100,100)
    
    # stores the width and height 
    width = screen.get_width()
    height = screen.get_height()
    
    # defining a font
    smallfont = pygame.font.SysFont('Corbel',35)
    
    # rendering a text written in this font
    text = smallfont.render('Humain vs IA' , True , color)
    text2 = smallfont.render('IA vs IA' , True , color) 
    
    while True:
        ######################################## INTERFACE #################################
        if mode == 5:
            for ev in pygame.event.get():
                
                if ev.type == pygame.QUIT:
                    print('mode',mode)
                    #pygame.quit()
                    
                #checks if a mouse is clicked
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    
                    #if the mouse is clicked on the
                    # button the game is terminated
                    if width/2-120 <= mouse[0] <= width/2+100 and height/2 - 270 <= mouse[1] <= height/2-190:
                        mode = 0
                        print('mode',mode)
                        #pygame.quit()
                        
                    elif width/2-120 <= mouse[0] <= width/2+100 and height/2 + 80  <= mouse[1] <= height/2 +160:
                        mode = 1
                        print('mode',mode)
                        #pygame.quit()
                        
            # fills the screen with a color
            screen.fill((60,25,60))
            
            # stores the (x,y) coordinates into
            # the variable as a tuple
            mouse = pygame.mouse.get_pos()

            
            # if mouse is hovered on a button it  
            if width/2-120 <= mouse[0] <= width/2+100 and height/2 - 270 <= mouse[1] <= height/2-190:
                # if mouse in box Humain vs IA -> lighter shade
                pygame.draw.rect(screen,color_light,[width/2-120,height/2-270,220,80])
                
            else:
                # else -> darker shade
                pygame.draw.rect(screen,color_dark,[width/2-120,height/2-270,220,80])          
            
            if width/2-120 <= mouse[0] <= width/2+100 and height/2 + 80  <= mouse[1] <= height/2 +160:
                # if mouse in box IA vs IA-> lighter shade
                pygame.draw.rect(screen,color_light,[width/2-120,height/2+80,220,80])
                
            else:
                # else -> darker shade
                pygame.draw.rect(screen,color_dark,[width/2-120,height/2+80,220,80])
            
            # superimposing the text onto our button
            screen.blit(text , (width/2-100,height/2-250))
            screen.blit(text2 , (width/2-70,height/2+100))
            
            # updates the frames of the game
            pygame.display.update()
        
        else :
            ######################################## CHECKERS BOT #################################
            
            ''' SOCKET CLIENT POUR COMMUNICATION TCP IP'''
            client_socket = client_program_init()
            
            game = checkers.Game(loop_mode=True)
        
            game.setup()
            bot = gamebot.Bot(game, RED, mid_eval='piece_and_board',
                            end_eval='sum_of_dist', method='alpha_beta', depth=3)
            random_bot_blue = gamebot.Bot(
                game, BLUE, mid_eval='piece_and_board_pov', method='alpha_beta', depth=3, end_eval='sum_of_dist')
            
            while True:  # main game loop  
                
                if mode == 0:  
                    if game.turn == BLUE:
                        # TO start player's turn uncomment the below line and comment a couple  of line below than that
                        # game.player_turn()
                        count_nodes = random_bot_blue.step(game.board, True)
                        game.update() #IA
                        
                        if gamebot.envoi_ia == 1:
                            position4 = C[gamebot.POSITION_PIECE_IA[0],gamebot.POSITION_PIECE_IA[1]]
                            position5 = C[gamebot.POSITION_PIECE_IA[2],gamebot.POSITION_PIECE_IA[3]]
                            position6 = C[gamebot.POSITION_PIECE_IA[4],gamebot.POSITION_PIECE_IA[5]]
                            position_ia = [position4, position5, position6]
                            client_program(client_socket, position_ia)
                            
                            #print('IA', position4, position5, position6)
                            gamebot.envoi_ia = 0     

             
                        #client_program(client_socket, position)
                    else:
                        # TO start player's turn uncomment the below line and comment a couple  of line below than that
                        #checkers.position_piece()
                        game.player_turn() #joueur
                        
                        if checkers.envoi == 1:
                            # Uncomment the below line for TCP IP communication 

                            position1 = C[checkers.POSITION_PIECE[0],checkers.POSITION_PIECE[1]]
                            position2 = C[checkers.POSITION_PIECE[2],checkers.POSITION_PIECE[3]]
                            position3 = C[checkers.POSITION_PIECE[4],checkers.POSITION_PIECE[5]] 
                            position_joueur = [position1, position2, position3]
                            client_program(client_socket, position_joueur)
                            #print('joueur',position1, position2, position3)
                            checkers.envoi = 0 

                        #count_nodes = bot.step(game.board, True)
                        #print('Total nodes explored in this step are', count_nodes)
                        #game.update()
                    if game.endit:
                        break
                if mode == 1:
                    if game.turn == BLUE:
                        count_nodes = random_bot_blue.step(game.board, True)
                        game.update() #IA
                        # Uncomment the below line for TCP IP communication 
                        position =gamebot.position_piece_ia()
                        client_program(client_socket, position)
                        
                    else:
                        count_nodes = bot.step(game.board, True)
                        game.update() #IA
                        position = gamebot.position_piece_ia()
                        client_program(client_socket, position)
                        

                    if game.endit:
                        break
              


if __name__ == "__main__":
    interface(mode)
    pass
