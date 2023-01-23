# Jeu de dames

https://github.com/Hsankesara/Draughts-AI

## Code

### Main

- checkers.py : plateau de jeu, pions, déplacements, visuels etc...

- gamebot.py : IA qui joue aux dames

- main.py : jeu de dames

Choix du mode de jeu Humain vs IA ou IA vs IA sur une interface (pygame). 

![image](https://user-images.githubusercontent.com/114569016/214103289-2eeb249b-e32d-4f71-9a63-04f3cc8eff22.png)

Puis jeu de dames (pygame)

![image](https://user-images.githubusercontent.com/114569016/211798485-7b8e71a6-fe51-4078-a56a-a9ad5bd48845.png)

### tests / Interface

tests/Interface/Checkers_Interface_bot : Interface jeu de dames avec la bibliotheque pygame (non finalisée)

bouton_mode_pygame.py : Interface choix mode avec la bibliotheque pygame

bouton_mode_test.py : Interface choix mode avec la bibliotheque PyQt

### tests / Test communication TCP IP

Tests communication client, serveur : https://github.com/ThenesVara/Checkers_Staubli/tree/main/Checkersbot_interface_TCPIP_Staubli/tests/Test%20communication%20TCP%20IP/Tests%20sockets#test-socket-communication-tcpip

Tests communication avec hercule : https://github.com/ThenesVara/Checkers_Staubli/tree/main/Checkersbot_interface_TCPIP_Staubli/tests/Test%20communication%20TCP%20IP#test-communication-tcpip

## Modification dans le code

- checkers.py :
Modifier le chemin de l'image du plateau de jeu

(ligne 190) : self.background = pygame.image.load(C:/Users/.../Draughts-AI-master/resources/board.png)
