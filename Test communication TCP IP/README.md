# Test communication TCP/IP

L'objectif est d'établir une connexion TCP/IP entre le Stäubli qui est serveur et votre ordinateur qui est client.
L'ordinateu est en connexion ethernet sur le contrôleur du Stäubli.

## Instructions modification d'adresse IP de votre ordianteur:

- Aller dans panneau de configuration - réseau et Internet - Connexion réseau

- Propriété ethernet 

![image](https://user-images.githubusercontent.com/114569016/210888205-6fbe7eff-c7b9-4b2f-9fbe-02ab3db238e2.png)


- Ouvrir le protocole internet version 4 (TCP/IPv4)

![image](https://user-images.githubusercontent.com/114569016/210888216-2ddd8e7c-bdde-420d-918e-4dfef8a6620c.png)


Sachant que l’adresse IP du port J205 sur le Stäubli est 172.31.0.1 et que son masque est 255.255.255.0.

- Modifier l’adresse IP de l’ordinateur : 172.31.0.XX . Remplacer le XX par une valeur quelconque (autre que celui occupé par le port J205 du Stäubli).

![image](https://user-images.githubusercontent.com/114569016/210888292-2566d60f-319d-4c5b-9397-e638376454a4.png)


- Valider les modifications

- Commande pour vérifier votre adresse IP sur le terminal avec la commande : 
```
ipconfig
```


## Test de communication avec Hercule

- Ouvrir le fichier hercules_3-2-8.exe

![image](https://user-images.githubusercontent.com/114569016/210888310-cb65f3c7-7220-4d7d-8713-a576faa6e7ac.png)

- Aller dans l’onglet : TCP Client (car l’ordinateur est client)

Renseigner l’adresse IP et le port du J205.
Dans notre cas : 172.31.0.1 et le port défini est : 5000

![image](https://user-images.githubusercontent.com/114569016/210888350-c82c2ab4-17ae-4abc-bb20-0b98637d7cc7.png)

- Cliquer sur Connect

![image](https://user-images.githubusercontent.com/114569016/210888372-7a55198b-06f0-44bc-bb90-198f48b3db0e.png)

- Lorsque vous êtes connecté, il est possible d’envoyer des messages de test dans la partie send. Cliquer sur send.

![image](https://user-images.githubusercontent.com/114569016/210888398-0b25c0bd-b7bc-4951-ae85-42ad1c5852b3.png)

- Ensuite le message envoyé au client est affiché :

![image](https://user-images.githubusercontent.com/114569016/210888423-a8049050-50a2-42c8-9f05-6db85fdcb0f8.png)


