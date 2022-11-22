#include<stdio.h>
#include<math.h>
#include<string.h>

#define TOUT_X 5 //5 si tout x est solution
#define AUCUNE 0 //0 si aucune solution
#define UNE_RACINE 1 //1 si racine simple
#define RACINE_DOUBLE 2//2 si racine double
#define DEUX_REELS 3// si 2 racine r�eles
#define DEUX_COMPLEXES 4// si 2 racines complexes


int poly2(double a, double b, double c, double*, double*);

void main()
{
	double a; //coeficiant devant x^2
	double b; //coeficiant devant x
	double c; //coeficiant constant
	double rac1 = 0; //initialisation racine1
	double rac2 = 0; //initialisation racine2
	printf("valeur de a:");
	scanf("%lf", &a);
	printf("valeur de b:");
	scanf("%lf", &b);
	printf("valeur de c:");
	scanf("%lf", &c);
	printf("Le resultat est de type: %d", poly2(a, b, c, &rac1, &rac2)); //returne le type du resultat
	switch (poly2(a,b,c,&rac1,&rac2)) //les cas possibles en fonction du determinant et des coeficiants
	{
	case AUCUNE:
		printf("\n");
		printf("aucune racine deso bg");
		break;
	case TOUT_X:
		printf("\n");
		printf("Tout X est racine");
		break;
	case UNE_RACINE:
		printf("\n");
		printf("racine_seule= %lf", rac1);
		break;
	case RACINE_DOUBLE:
		printf("\n");
		printf("racine_double= %2.lf", rac1);
		break;
	case DEUX_REELS:
		printf("\n");
		printf("racine_reele1= %2.lf racine_reele2= %2.lf", rac1, rac2);
		break;
	case DEUX_COMPLEXES:
		printf("\n");
		printf("racine_complexe1=  %.2lf + %.2lfi racine_complexe2=  %.2lf - %.2lfi", rac1, rac2,rac1,rac2);
		break;
	default:
		break;
	}
	return 0;
}

int poly2(double a, double b, double c, double* racine1, double* racine2) //racine1 et racine2 sont des pointeurs
{
	double delta;
	delta = b * b - 4 * a * c; //calcule le discriminant
	if (a == 0 && b == 0 && c == 0) // condition pour avoir tout x comme solution
	{
		return TOUT_X; //car tout x est solution
	}
	else if (a == 0 && b == 0) //condition pour aucune racine
	{
		return AUCUNE; //car aucune solution
	}
	else if (a == 0) //condition pour 1 seul racine
	{
		*racine1 = (-c / b); //calcule la racine
		return UNE_RACINE; //car une seule racine
	}
	else if (delta == 0) //condition pour racine double
	{
		*racine1 = (-b - sqrt(delta)) / (2 * a); //calcule la racine
		return RACINE_DOUBLE; //car racine doube
	}
	else if (delta > 0) //condition pour 2 racines r�eles
	{
		*racine2 = (-b + sqrt(delta)) / (2 * a); //calcule la 1ere racine
		*racine1 = (-b - sqrt(delta)) / (2 * a);	//calcule la 2eme racine
		return DEUX_REELS; //car 2 racine r�eles 
	}
	else if (delta < 0) //condition pour 2 racines complexes
	{
		*racine1 = -b / (2 * a); //calcule la pratie r�ele
		*racine2 = sqrt(fabs(delta)) / (2 * a); //calcule la partie imaginaire
		return DEUX_COMPLEXES; //car 2 racine complexes
	}
}