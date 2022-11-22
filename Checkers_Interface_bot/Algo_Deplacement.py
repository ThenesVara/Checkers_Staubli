
#partie calcul pour le, projet checker's board 
import numpy as np

mat_test=[1,0,-1] #1 présence de pion noir, 0 aucune présence, -1 présence de pion blanc

board=[ [64, 64,1],[184, 64,1],[304, 64,1],[424, 64,1],
        [124, 124,1],[244, 124,1],[364, 124,1],[484, 124,1],
        [64, 184,1],[184, 184,1],[304, 184,1],[424, 184,1],
        [124, 244,0],[244, 244,0],[364, 244,0],[484, 244,0],
        [64, 304,0],[184, 304,0],[304, 304,0],[424, 304,0],
        [124, 364,-1],[244, 364,-1],[364, 364,-1],[484, 364,-1],
        [64, 424,-1],[184, 424,-1],[304, 424,-1],[424, 424,-1],
        [484, 364,-1],[484, 364,-1],[484, 364,-1],[484, 484,-1],

        ]

def deplacement_pion(case_D,case_A):
    # dans cette partie on modifie la matrice contenant la position sur le damier et ce qui est présent à cette emplacement 
    if case_A[3] == 0:

        if( case_D[3] == 1):

            if (case_D[2]+60 == case_A[2]):

                if (case_D[1]+60 == case_A[2] or case_D[1]-60 == case_A[2]):

                    case_A[3]=case_D[3] #le pion est maintenant considéré comme arrivé dans la case_Arrive
                    case_D[3]=0 #il n'y a maintenant  plus rien dans la case de depart
                    
                    return 1 #

            else:
                print("déplacement invalide")

        elif(case_D[3] == - 1):

            if (case_D[2]- 60 == case_A[2]):

                if (case_D[1]+60 == case_A[2] or case_D[1]-60 == case_A[2]):

                    case_A[3]=case_D[3] #le pion est maintenant considéré comme arrivé dans la case_Arrive
                    case_D[3]=0 #il n'y a maintenant  plus rien dans la case de depart

        else:

            print("pas besoin de deplacer une case vide")
    else:
        print('déplacement impossible')



def manger_pion(case_D,case_Ar,case_En):
    return 0



    



