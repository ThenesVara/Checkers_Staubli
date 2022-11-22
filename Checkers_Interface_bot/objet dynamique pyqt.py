from json import load
import sys
from PyQt5.QtWidgets import QLabel, QApplication, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QPushButton
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize, QRect, QPointF

#Point fixe sur le plateau

Point_fixe=[]
class MovingObject(QGraphicsEllipseItem):
    def __init__(self, x, y, r):
        super().__init__(0, 0, r, r)
        self.setPos(x, y)
        self.setBrush(Qt.darkYellow)
        self.setAcceptHoverEvents(True)

    # mouse hover event
    def hoverEnterEvent(self, event):
        app.instance().setOverrideCursor(Qt.OpenHandCursor)

    def hoverLeaveEvent(self, event):
        app.instance().restoreOverrideCursor()

    # mouse click event
    def mousePressEvent(self, event):
        pass

    def mouseMoveEvent(self, event):
        print(self)
        orig_cursor_position = event.lastScenePos()
        updated_cursor_position = event.scenePos()
        orig_position = self.scenePos()

        updated_cursor_x = updated_cursor_position.x() - orig_cursor_position.x() + orig_position.x()
        updated_cursor_y = updated_cursor_position.y() - orig_cursor_position.y() + orig_position.y()
        self.setPos(QPointF(updated_cursor_x, updated_cursor_y))

    def mouseReleaseEvent(self, event):
        print('x: {0}, y: {1}'.format(self.pos().x(), self.pos().y()))

class GraphicView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.img = QPixmap("Boardel.jpg") #On crée un élément Pixmap
        pixmap_resized = self.img.scaled(600,600)  #on le met à la taille de notre scene
        self.rotation = 90
        transr = QtGui.QTransform().rotate(self.rotation)
        pixmap_resized = pixmap_resized.transformed(transr,Qt.SmoothTransformation) 
        self.scene = QGraphicsScene()  #On crée un élément scene sur lequel on ajoute nos objets dynamique
        self.setScene(self.scene) #affiche la scene 
        #self.setSceneRect(0, 0, 1000, 1200) #met la scene sous forme de rectangle
        self.label = QtWidgets.QLabel()
        self.scene.addPixmap(pixmap_resized) #on ajoute notre pixamp a la scene

        #création d'un bouton setup:
        self.setupButton = QPushButton(self)
        self.setupButton.setText("setup")          #text
        #self.setupButton.setShortcut('Ctrl+D')  #shortcut key
        self.setupButton.clicked.connect(self.setup) #ferme la fenetre
        self.setupButton.move(5,5)

        self.reset=QPushButton(self)
        self.reset.setText("restart")          #text
        #self.restart.setShortcut('Ctrl+D')  #shortcut key
        self.reset.clicked.connect(self.restart) #ferme la fenetre
        self.reset.move(5,25)

        self.delButton = QPushButton(self)
        self.delButton.setText("delete")          #text
        self.delButton.setShortcut('Ctrl+D')  #shortcut key
        self.delButton.clicked.connect(self.delete) #ferme la fenetre
        self.delButton.move(5,50)







 
            


           

    #fonction setup

    def setup(self) :
        



        self.moveObject_noir1 = MovingObject(124, 64, 50)
        self.moveObject_noir2 = MovingObject(244, 64, 50) #ajoute un objet de taille 50 a la position 125 en x et 50 en y
        self.moveObject_noir3 = MovingObject(364, 64, 50) 
        self.moveObject_noir4 = MovingObject(484, 64, 50) 
        self.moveObject_noir5 = MovingObject(64, 124, 50)
        self.moveObject_noir6 = MovingObject(184, 124, 50) #ajoute un objet de taille 50 a la position 125 en x et 50 en y
        self.moveObject_noir7 = MovingObject(304, 124, 50) 
        self.moveObject_noir8 = MovingObject(424, 124, 50)  
        self.moveObject_noir9 = MovingObject(124, 184, 50)
        self.moveObject_noir10 = MovingObject(244, 184, 50) #ajoute un objet de taille 50 a la position 125 en x et 50 en y
        self.moveObject_noir11 = MovingObject(364, 184, 50) 
        self.moveObject_noir12 = MovingObject(484, 184, 50)     

        

        #creation des objets pions blancs 
        self.moveObject_blanc1 = MovingObject(64, 484, 50)
        self.moveObject_blanc2 = MovingObject(184, 484, 50)
        self.moveObject_blanc3 = MovingObject(304, 484, 50) 
        self.moveObject_blanc4 = MovingObject(424, 484, 50) 
        self.moveObject_blanc5 = MovingObject(124, 424, 50)
        self.moveObject_blanc6 = MovingObject(244, 424, 50) 
        self.moveObject_blanc7 = MovingObject(364, 424, 50) 
        self.moveObject_blanc8 = MovingObject(484, 424, 50)  
        self.moveObject_blanc9 = MovingObject(64, 364, 50)
        self.moveObject_blanc10 = MovingObject(184, 364, 50) 
        self.moveObject_blanc11 = MovingObject(304, 364, 50) 
        self.moveObject_blanc12 = MovingObject(424, 364, 50)



        self.scene.removeItem(self.moveObject_blanc1)
        self.scene.removeItem(self.moveObject_blanc2)
        self.scene.removeItem(self.moveObject_blanc3)
        self.scene.removeItem(self.moveObject_blanc4)
        self.scene.removeItem(self.moveObject_blanc5)
        self.scene.removeItem(self.moveObject_blanc6)
        self.scene.removeItem(self.moveObject_blanc7)
        self.scene.removeItem(self.moveObject_blanc8)
        self.scene.removeItem(self.moveObject_blanc9)
        self.scene.removeItem(self.moveObject_blanc10)
        self.scene.removeItem(self.moveObject_blanc11)
        self.scene.removeItem(self.moveObject_blanc12)

        self.scene.removeItem(self.moveObject_noir1) 
        self.scene.removeItem(self.moveObject_noir2) 
        self.scene.removeItem(self.moveObject_noir3)
        self.scene.removeItem(self.moveObject_noir4)
        self.scene.removeItem(self.moveObject_noir5) 
        self.scene.removeItem(self.moveObject_noir6) 
        self.scene.removeItem(self.moveObject_noir7)
        self.scene.removeItem(self.moveObject_noir8)
        self.scene.removeItem(self.moveObject_noir9) 
        self.scene.removeItem(self.moveObject_noir10) 
        self.scene.removeItem(self.moveObject_noir11)
        self.scene.removeItem(self.moveObject_noir12) 
                # on ajoute les items noir sur la scene
        
        self.scene.addItem(self.moveObject_noir1) 
        self.scene.addItem(self.moveObject_noir2) 
        self.scene.addItem(self.moveObject_noir3)
        self.scene.addItem(self.moveObject_noir4)
        self.scene.addItem(self.moveObject_noir5) 
        self.scene.addItem(self.moveObject_noir6) 
        self.scene.addItem(self.moveObject_noir7)
        self.scene.addItem(self.moveObject_noir8)
        self.scene.addItem(self.moveObject_noir9) 
        self.scene.addItem(self.moveObject_noir10) 
        self.scene.addItem(self.moveObject_noir11)
        self.scene.addItem(self.moveObject_noir12)


        self.scene.addItem(self.moveObject_blanc1) 
        self.scene.addItem(self.moveObject_blanc2) 
        self.scene.addItem(self.moveObject_blanc3)
        self.scene.addItem(self.moveObject_blanc4)
        self.scene.addItem(self.moveObject_blanc5) 
        self.scene.addItem(self.moveObject_blanc6) 
        self.scene.addItem(self.moveObject_blanc7)
        self.scene.addItem(self.moveObject_blanc8)
        self.scene.addItem(self.moveObject_blanc9) 
        self.scene.addItem(self.moveObject_blanc10) 
        self.scene.addItem(self.moveObject_blanc11)
        self.scene.addItem(self.moveObject_blanc12)

    #fonction delete correspondant au bouton 
    def delete(self):
                        #on supprime tous les items de scene

        self.scene.removeItem(self.moveObject_blanc1)
        self.scene.removeItem(self.moveObject_blanc2)
        self.scene.removeItem(self.moveObject_blanc3)
        self.scene.removeItem(self.moveObject_blanc4)
        self.scene.removeItem(self.moveObject_blanc5)
        self.scene.removeItem(self.moveObject_blanc6)
        self.scene.removeItem(self.moveObject_blanc7)
        self.scene.removeItem(self.moveObject_blanc8)
        self.scene.removeItem(self.moveObject_blanc9)
        self.scene.removeItem(self.moveObject_blanc10)
        self.scene.removeItem(self.moveObject_blanc11)
        self.scene.removeItem(self.moveObject_blanc12)

        self.scene.removeItem(self.moveObject_noir1) 
        self.scene.removeItem(self.moveObject_noir2) 
        self.scene.removeItem(self.moveObject_noir3)
        self.scene.removeItem(self.moveObject_noir4)
        self.scene.removeItem(self.moveObject_noir5) 
        self.scene.removeItem(self.moveObject_noir6) 
        self.scene.removeItem(self.moveObject_noir7)
        self.scene.removeItem(self.moveObject_noir8)
        self.scene.removeItem(self.moveObject_noir9) 
        self.scene.removeItem(self.moveObject_noir10) 
        self.scene.removeItem(self.moveObject_noir11)
        self.scene.removeItem(self.moveObject_noir12)

    def restart(self):

        self.scene.removeItem(self.moveObject_blanc1)
        self.scene.removeItem(self.moveObject_blanc2)
        self.scene.removeItem(self.moveObject_blanc3)
        self.scene.removeItem(self.moveObject_blanc4)
        self.scene.removeItem(self.moveObject_blanc5)
        self.scene.removeItem(self.moveObject_blanc6)
        self.scene.removeItem(self.moveObject_blanc7)
        self.scene.removeItem(self.moveObject_blanc8)
        self.scene.removeItem(self.moveObject_blanc9)
        self.scene.removeItem(self.moveObject_blanc10)
        self.scene.removeItem(self.moveObject_blanc11)
        self.scene.removeItem(self.moveObject_blanc12)

        self.scene.removeItem(self.moveObject_noir1) 
        self.scene.removeItem(self.moveObject_noir2) 
        self.scene.removeItem(self.moveObject_noir3)
        self.scene.removeItem(self.moveObject_noir4)
        self.scene.removeItem(self.moveObject_noir5) 
        self.scene.removeItem(self.moveObject_noir6) 
        self.scene.removeItem(self.moveObject_noir7)
        self.scene.removeItem(self.moveObject_noir8)
        self.scene.removeItem(self.moveObject_noir9) 
        self.scene.removeItem(self.moveObject_noir10) 
        self.scene.removeItem(self.moveObject_noir11)
        self.scene.removeItem(self.moveObject_noir12)

        self.scene.addItem(self.moveObject_noir1) 
        self.scene.addItem(self.moveObject_noir2) 
        self.scene.addItem(self.moveObject_noir3)
        self.scene.addItem(self.moveObject_noir4)
        self.scene.addItem(self.moveObject_noir5) 
        self.scene.addItem(self.moveObject_noir6) 
        self.scene.addItem(self.moveObject_noir7)
        self.scene.addItem(self.moveObject_noir8)
        self.scene.addItem(self.moveObject_noir9) 
        self.scene.addItem(self.moveObject_noir10) 
        self.scene.addItem(self.moveObject_noir11)
        self.scene.addItem(self.moveObject_noir12)


        self.scene.addItem(self.moveObject_blanc1) 
        self.scene.addItem(self.moveObject_blanc2) 
        self.scene.addItem(self.moveObject_blanc3)
        self.scene.addItem(self.moveObject_blanc4)
        self.scene.addItem(self.moveObject_blanc5) 
        self.scene.addItem(self.moveObject_blanc6) 
        self.scene.addItem(self.moveObject_blanc7)
        self.scene.addItem(self.moveObject_blanc8)
        self.scene.addItem(self.moveObject_blanc9) 
        self.scene.addItem(self.moveObject_blanc10) 
        self.scene.addItem(self.moveObject_blanc11)
        self.scene.addItem(self.moveObject_blanc12)
        
         


class main_window(object):
    def __init_(self,dialog):
        app = QApplication(sys.argv)
        win = QWidget()
        win.setMinimumSize(1000, 1000)
        vbox = QVBoxLayout()
        self.label = QLabel(win)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self;vbox.addWidget(self.label)
        win.setLayout(vbox)
        win.setWindowTitle("QLabel Demo")
        win.show()
        sys.exit(app.exec_())
        #self.setup = setup.

app = QApplication(sys.argv)
view = GraphicView()
view.show()
sys.exit(app.exec_())

#creation d'une matrice  8 8 avec 1 0 -1 1-> noir 0 libre et -1 blanc