import checkers
import gamebot
from time import sleep
import pygame
import sys

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


def interface(mode): 
    '''PARAMETRES INTERFACE'''
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
            ######################################## CHECKERS #################################
            
            #client_socket = checkers.client_program_init()
            
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
                        game.update()
                        #checkers.client_program(client_socket)
                    else:
                        # TO start player's turn uncomment the below line and comment a couple  of line below than that
                        game.player_turn()
                        #checkers.client_program(client_socket)
                        
                        #count_nodes = bot.step(game.board, True)
                        #print('Total nodes explored in this step are', count_nodes)
                        #game.update()
                    if game.endit:
                        break
                if mode == 1:
                    if game.turn == BLUE:
                        # TO start player's turn uncomment the below line and comment a couple  of line below than that
                        # game.player_turn()
                        count_nodes = random_bot_blue.step(game.board, True)
                        game.update()
                        #checkers.client_program(client_socket)
                        
                    else:
                        # TO start player's turn uncomment the below line and comment a couple  of line below than that
                        # game.player_turn()
                        count_nodes = bot.step(game.board, True)
                        game.update()
                        #checkers.client_program(client_socket)
                        

                    if game.endit:
                        break
              


if __name__ == "__main__":
    interface(mode)
    pass
