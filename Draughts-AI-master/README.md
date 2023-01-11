# Jeu de dames

checkers.py : plateau de jeu, pions, déplacements, visuels etc...

gamebot.py : IA qui joue aux dames

main.py : jeu de dames 
-> mode 0 : Humain VS IA 
-> mode 1 : IA VS IA

main_interface.py : Choix du mode de jeu Humain vs IA ou IA vs IA sur une interface. Puis jeu de dames


## Modification 
checkers.py :
- Modifier le chemin de l'image du plateau de jeu
(ligne 190) : self.background = pygame.image.load(*CHEMIN_DU_PLATEAU_RESOURCES*)

exemple : CHEMIN_DU_PLATEAU_RESOURCES : C:/Users/.../Draughts-AI-master/resources/board.png