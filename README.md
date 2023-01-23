# Checkers_Staubli

Notre objectif pour ce projet est de faire jouer aux dames un robot de type Stäubli TX-90. Celui-ci pourra permetre aux travers d'une IHM de voir 2 personnes s'affronter
ou bien une personne affronter une IA. 

Pour ceci, nous allons créer un environnement de simulation sous SRS, une IHM afin que l'utilisateur puisse jouer. Les mouvements effectuées sur l'interface seront envoyés à au controleur du TX-90 grâce à une carte de type Raspberry PI liée au robot via une communication TCP/IP. 


# SRS environment 

- Environnement :

<img src="https://user-images.githubusercontent.com/114569016/203329509-b680678e-07d7-4dbc-9639-2bb0f35bf0fb.PNG" width=30% height=30%>

- Notre plateau de jeu : Une case correspond à un numéro

<img src="https://user-images.githubusercontent.com/114569016/214121722-85b692c8-693a-4eb6-b142-121b309f90bc.jpg" width=30% height=30%>

Fonctions : 

- CasesNoires() : calcule la position des cases noires en fonction de la case 0

- Déplacementpion(départ, arrivée): cette fonction déplace un pion d'un point départ à un point arrivée (en utilisant pCasesNoires)

- Pionperdu(casepionperdu, compteur) : cette fonction déplace un pion perdu dans une zone "perdu"

- Dataacqu(): récupère les valeurs envoyés par TCP IP depuis l'ordinateur (donnee1, donnee1, donnee3)


# Checkersbot 

## Interface pygame

Choix du mode de jeu :

<img src="https://user-images.githubusercontent.com/114569016/214119392-c06661de-c22b-41a4-8bb2-799a03f69cbf.png" width=30% height=30%>

## Jeu de dames 

Jeu selon le mode choisi :

<img src="https://user-images.githubusercontent.com/114569016/214119823-506b189a-ed3a-4d0f-a0f9-e424da921871.png" width=30% height=30%>

Possibilité de jouer sans communication, sans le Stäubli :

Dans le main.py , commenter : 

- client_socket = checkers.client_program_init()
- checkers.client_program(client_socket)

