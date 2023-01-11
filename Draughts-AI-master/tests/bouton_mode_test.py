# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


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


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
