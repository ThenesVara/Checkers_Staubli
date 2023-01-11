import checkers
import gamebot
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
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




class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Checkers Game")

		# setting geometry
		self.setGeometry(100, 100, 600, 400)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()
 
  	# action method
	def mode2(self):
		# printing pressed
		print("Mode Humain vs Ordi")
		modegame=0
		print('modegame', modegame)
  
	def mode(self):
		print("Mode Ordi vs Ordi")
		modegame=1
		print('modegame',modegame)
  
	# method for widgets
	def UiComponents(self):

		# creating a push button
		button = QPushButton("Humain VS Humain", self)
		# setting size of button
		button.resize(450, 150)

		# adding action to a button
		button.clicked.connect(self.mode)
		button.move(5,5)
  
        # creating a push button
		button2 = QPushButton("Humain VS Machine", self)
		# setting size of button
		button2.resize(450,150)
		# adding action to a button
		button2.clicked.connect(self.mode2)
		button2.move(5,170)


	
  
  

  

  

# mode 0 : Humain VS IA
# mode 1 : IA VS IA



def main():
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    # start the app
    modegame=2
    
    while True:
        
        game = checkers.Game(loop_mode=True)
        
        game.setup()
        bot = gamebot.Bot(game, RED, mid_eval='piece_and_board',
                          end_eval='sum_of_dist', method='alpha_beta', depth=3)
        random_bot_blue = gamebot.Bot(
            game, BLUE, mid_eval='piece_and_board_pov', method='alpha_beta', depth=3, end_eval='sum_of_dist')
        
        while True:  # main game loop
            if modegame == 0:
                '''
                board = checkers.Board()
                print('board', board.repr_matrix())
                '''
                # MATRICE AVEC LES POSITIONS DES PIONS
                #print('board', game.board.repr_matrix())
                
                if game.turn == BLUE:
                    # TO start player's turn uncomment the below line and comment a couple  of line below than that
                    # game.player_turn()
                    count_nodes = random_bot_blue.step(game.board, True)
                    #print('Total nodes explored in this step are', count_nodes)
                    game.update()
                else:
                    # TO start player's turn uncomment the below line and comment a couple  of line below than that
                    game.player_turn()
                    #count_nodes = bot.step(game.board, True)
                    #print('Total nodes explored in this step are', count_nodes)
                    #game.update()
                if game.endit:
                    break

            if modegame == 1:
                if game.turn == BLUE:
                    # TO start player's turn uncomment the below line and comment a couple  of line below than that
                    # game.player_turn()
                    count_nodes = random_bot_blue.step(game.board, True)
                    #print('Total nodes explored in this step are', count_nodes)
                    game.update()
                else:
                    # TO start player's turn uncomment the below line and comment a couple  of line below than that
                    # game.player_turn()
                    count_nodes = bot.step(game.board, True)
                    #print('Total nodes explored in this step are', count_nodes)
                    game.update()

                if game.endit:
                    break
                
            else:
                break
        sys.exit(App.exec())



if __name__ == "__main__":
    main()
    '''
    if window.UiComponents():
        mode = 0
        print(mode)
    if QPushButton("Humain VS Machine")==True:
        mode = 1 
        print(mode)
        
    print(mode)'''
    
    '''if mode == 0 or mode == 1 :
        #window.close()
         
        #main(mode)
    pass'''
