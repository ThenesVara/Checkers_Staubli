# Jeu de dames

https://github.com/Hsankesara/Draughts-AI

## Code

- checkers.py : plateau de jeu, pions, déplacements, visuels etc...

- gamebot.py : IA qui joue aux dames

- main.py : jeu de dames 

-> mode 0 : Humain VS IA 

-> mode 1 : IA VS IA

![image](https://user-images.githubusercontent.com/114569016/211798485-7b8e71a6-fe51-4078-a56a-a9ad5bd48845.png)

- main_interface.py : Choix du mode de jeu Humain vs IA ou IA vs IA sur une interface. Puis jeu de dames

![image](https://user-images.githubusercontent.com/114569016/211798756-a9571dd7-5fe7-4110-b4bc-fbbc51d8a897.png)


## Modification dans le code

- checkers.py :
Modifier le chemin de l'image du plateau de jeu

(ligne 190) : self.background = pygame.image.load(C:/Users/.../Draughts-AI-master/resources/board.png)
