# Test communication TCP/IP

L'objectif est d'établir une connexion TCP/IP entre le Stäubli qui est serveur et votre ordinateur qui est client.
L'ordinateu est en connexion ethernet sur le contrôleur du Stäubli.

## Instructions modification d'adresse IP de votre ordianteur:

- Aller dans panneau de configuration - réseau et Internet - Connexion réseau

- Propriété ethernet 

- Ouvrir le protocole internet version 4 (TCP/IPv4)

Sachant que l’adresse IP du port J205 sur le Stäubli est 172.31.0.1 et que son masque est 255.255.255.0.

- Modifier l’adresse IP de l’ordinateur : 172.31.0.XX . Remplacer le XX par une valeur quelconque (autre que celui occupé par le port J205 du Stäubli).

- Valider les modifications

- Commande pour vérifier votre adresse IP sur le terminal avec la commande : 
```
ipconfig
```


## Test de communication avec Hercule

- Ouvrir le fichier hercules_3-2-8.exe

- Aller dans l’onglet : TCP Client (car l’ordinateur est client)

Renseigner l’adresse IP et le port du J205.
Dans notre cas : 172.31.0.1 et le port défini est : 5000

- Cliquer sur Connect

- Lorsque vous êtes connecté, il est possible d’envoyer des messages de test dans la partie send. Cliquer sur send.

- Ensuite le message envoyé au client est affiché :

