''' Interface mode avec pygame
    Tutoriel : https://stacklima.com/comment-creer-des-boutons-dans-un-jeu-en-utilisant-pygame/
'''

import pygame
import sys
  

global mode 
mode = 5

# initializing the constructor
pygame.init()
  
# screen resolution
res = (720,720)
  
# opens up a window
screen = pygame.display.set_mode(res)
  
# white color
color = (255,255,255)
  
# light shade of the button
color_light = (170,170,170)
  
# dark shade of the button
color_dark = (100,100,100)
  
# stores the width of the
# screen into a variable
width = screen.get_width()
  
# stores the height of the
# screen into a variable
height = screen.get_height()
  
# defining a font
smallfont = pygame.font.SysFont('Corbel',35)


# rendering a text written in
# this font
text = smallfont.render('Humain vs IA' , True , color)
text2 = smallfont.render('IA vs IA' , True , color)


def interface():  
    while True:
        
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
              

if __name__ == "__main__":
    interface()
    return_mode()
