#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#   main.py
#   ==> programme de recommandation de livres avec gestion des livres et des profils
#   ==> détails dans le README
#
#   Auteurs: Maël Aubert, Marius Chevailler
#----------------------------------------------------------------------------

# Importation des fonctions externes
from profils import *
from livres import *
from recommandation import *

# Fonctions des menus
def menu_profils():
    continuer = True
    while continuer: # boucle pour réafficher le menu des profils jusqu'à la fermeture du programme

        ## menu des profils
        print("      ----- Gestion des profils -----")
        print("   1 - Ajouter un profil")
        print("   2 - Voir un profil")
        print("   3 - Modifier un profil")
        print("   4 - Supprimer un profil")
        print("   5 - Retour")
        choix = input("\nPour faire votre choix, entrez 1, 2, 3, 4, ou 5 : ")
        while choix not in {"1", "2", "3", "4", "5", "6"}:  ##Saisie sécurisée
            choix = input("Erreur... "+ choix +" n'est pas compris dans 1, 2, 3, 4, 5 ou 6 : ")
        print("")

        choix = int(choix)
        if choix == 1: ajout_profil()
        elif choix == 2: voir_profil()
        elif choix == 3: modifier_profil() #todo modification d'un profil
        elif choix == 4: suppr_profil()
        elif choix == 5: continuer = False

def menu_livres():
    continuer = True
    while continuer:  # boucle pour réafficher le menu des profils en boucle jusqu'à la fermeture du programme

        ## menu des profils
        print("      ----- Gestion des livres -----")
        print("   1 - Voir la liste des livres")
        print("   2 - Ajouter un livre")
        print("   3 - Modifier un livre")
        print("   4 - Supprimer un livre")
        print("   5 - Retour")
        choix = input("\nPour faire votre choix, entrez 1, 2, 3, 4, ou 5 : ")
        while choix not in {"1", "2", "3", "4", "5", "6"}:  ##Saisie sécurisée
            choix = input("Erreur... " + choix + " n'est pas compris dans 1, 2, 3, 4, 5 ou 6 : ")
        print("")

        choix = int(choix)
        if choix == 1:
            ajouter_booksread()
        elif choix == 2:
            ajout_livre()
        elif choix == 3:
            modifier_livre()
        elif choix == 4:
            supprimer_livre()
        elif choix == 5:
            continuer = False


def menu_recommandation():
    print("recommandation")
    continuer = True
    while continuer:  # boucle pour réafficher le menu des recommandations en boucle jusqu'à la fermeture du programme
        ## menu de la partie recommandation
        print("      ----- Recommandations -----")
        print("   1 - Noter un livre")
        print("   2 - Suggérer un livre")
        print("   3 - Afficher matrice de notation (!!! temporaire !!!)")
        print("   4 - Afficher matrice de similarité (!!! temporaire !!!)")
        print("   5 - Retour")
        choix = input("\nPour faire votre choix, entrez 1, 2, 3, 4, ou 5 : ")
        while choix not in {"1", "2", "3", "4", "5", "6"}:  ##Saisie sécurisée
            choix = input("Erreur... " + choix + " n'est pas compris dans 1, 2, 3, 4, 5 ou 6 : ")
        print("")

        choix = int(choix)
        if choix == 1:
            noter_livre() ## permet de noter un livre
        elif choix == 2:
            suggerer_livres() ## permet de chercher un livre selon les notes et les livres lus
        elif choix == 3:
            afficher_notation() ## permet d'afficher la matrice de notation ( !!! temporaire !!!)
        elif choix == 4:
            afficher_similarite() ## permet d'afficher le profil le plus proche du sien (!!! temporaire !!!)
        elif choix == 5:
            continuer = False


#############################
# Corps du programme principal
if __name__ == '__main__':
    creer_matrice_notation()
    continuer = True
    while continuer:  ## boucle pour réafficher le menu principal en boucle jusqu'à la fermeture du programme

        ## menu principal
        print("      ------ Menu principal ------")
        print("   1 - Profils des lecteurs")
        print("   2 - Visiter le dépôt des livres")
        print("   3 - Recommandation")
        print("   4 - Quitter")
        choix = input("\nPour faire votre choix, entrez 1, 2, 3 ou 4 : ")
        while choix not in {"1", "2", "3", "4"}:  ## Saisie sécurisée
            choix = input("Erreur... " + choix + " n'est pas compris dans 1, 2, 3 ou 4 : ")
        print("")

        choix = int(choix)
        if choix == 1:
            menu_profils()  ## lance la fonction de gestion du profils des lecteurs
        elif choix == 2:
            menu_livres()  ## lance la fonction de gestion du dépôt des livres
        elif choix == 3:
            menu_recommandation()  ## lance la fonction de recommandation d'un livre
        else:
            continuer = False  ## permet de quitter la boucle et fermer le programme

    afficher_notation()
    print("      ------ Fin du programme ------")