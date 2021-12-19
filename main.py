#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#   main.py
#       ==> initialise le programme (élimination des éléments pouvant entrainer des bugs, vérification des fichiers [format, etc..])
#       ==> regroupe la boucle principal du menu ainsi que les sous-menus permettant d'accéder aux fonctionnalitées du programme.
#
#   Auteurs: Maël Aubert, Marius Chevailler
# ----------------------------------------------------------------------------


# Importation des fonctions externes
from profils import *
from livres import *
from recommandation import *


# Fonctions des menus

def menu_profils():
    continuer = True
    while continuer:  # boucle pour réafficher le menu des profils jusqu'au choix du retour
        print("      ----- Gestion des profils -----")
        print("   1 - Ajouter un profil")
        print("   2 - Voir un profil")
        print("   3 - Modifier un profil")
        print("   4 - Supprimer un profil")
        print("   5 - Retour")
        choix = input("\nPour faire votre choix, entrez 1, 2, 3, 4, ou 5 : ")
        while choix not in {"1", "2", "3", "4", "5", "6"}:  #Saisie sécurisée
            choix = input("Erreur... " + choix + " n'est pas compris dans 1, 2, 3, 4, 5 ou 6 : ")
        print("\n")

        choix = int(choix)
        if choix == 1:
            ajout_profil() #permet d'ajouter un profil (modification des fichiers associés au profil)
        elif choix == 2:
            voir_profil() #permet d'afficher les informations d'un profil
        elif choix == 3:
            modifier_profil() #permet de modifier les informations d'un profil (modification du fichier readers.txt)
        elif choix == 4:
            suppr_profil() #permet de supprimer un profil (modification des fichiers associés au profil)
        elif choix == 5:
            continuer = False #retour au menu principal


def menu_livres():
    continuer = True
    while continuer:  # boucle pour réafficher le menu des livres jusqu'au choix du retour
        print("      ----- Gestion des livres -----")
        print("   1 - Voir la liste des livres")
        print("   2 - Lire un livre")
        print("   3 - Ajouter un livre")
        print("   4 - Modifier un livre")
        print("   5 - Supprimer un livre")
        print("   6 - Retour")
        choix = input("\nPour faire votre choix, entrez 1, 2, 3, 4, 5, ou 6 : ")
        while choix not in {"1", "2", "3", "4", "5", "6"}:  #Saisie sécurisée
            choix = input("Erreur... " + choix + " n'est pas compris dans 1, 2, 3, 4, 5 ou 6 : ")
        print("\n")

        choix = int(choix)
        if choix == 1:
            afficher_livres() #permet d'afficher la liste des livres
        elif choix == 2:
            lire_livre() #permet d'ajouter un livre à la liste des livres lus
        elif choix == 3:
            ajout_livre() #permet d'ajouter un livre à la liste des livres
        elif choix == 4:
            modifier_livre() #permet de modifier le titre d'un livre
        elif choix == 5:
            supprimer_livre() # permet de supprimer un livre (modifications dans les fichiers associés au livre [décalage des données dans les fichiers])
        elif choix == 6:
            continuer = False # retour au menu principal


def menu_recommandation():
    continuer = True
    while continuer:  # boucle pour réafficher le menu des recommendations jusqu'au choix du retour
        print("      ----- Recommandations -----")
        print("   1 - Noter un livre")
        print("   2 - Suggérer un livre")
        print("   3 - Retour")
        choix = input("\nPour faire votre choix, entrez 1, 2 ou 3 : ")
        while choix not in {"1", "2", "3"}:  #Saisie sécurisée
            choix = input("Erreur... " + choix + " n'est pas compris dans 1, 2 ou 3: ")
        print("\n")

        choix = int(choix)
        if choix == 1:
            noter_livre()  # permet d'ajouter une note d'un livre dans la matrice de notation
        elif choix == 2:
            suggerer_livres()  # permet de suggérer un livre selon les notes et les livres lus par les utilisateurs
        elif choix == 3:
            continuer = False # retour au menu principal


def menu_reinitialiser():
    continuer = True
    while continuer:  # boucle pour réafficher le menu des recommandations en boucle jusqu'à la fermeture du programme
        ## menu de la partie recommandation
        print("      ----- Réinitialisation -----")
        print("Voulez vous réinitialiser : ")
        print("   1 - Profils")
        print("   2 - Liste des livres lus")
        print("   3 - Livres stockés")
        print("   4 - Notes\n")
        print("   5 - Retour")
        choix = input("\nPour faire votre choix, entrez 1, 2, 3, 4 ou 5 : ")
        while choix not in {"1", "2", "3", "4", "5"}:  ##Saisie sécurisée
            choix = input("Erreur... " + choix + " n'est pas compris dans 1, 2, 3, 4 ou 5 : ")
        print("\n")

        choix = int(choix)
        if choix == 1:
            reinitialiser("profils") # supprime tous les profils dans 'readers.txt' et dans 'booksread.txt'
        elif choix == 2:
            reinitialiser("lectures") # supprime les numéros des livres lus dans le fichier 'booksread.txt'
        elif choix == 3:
            reinitialiser("livres") # supprime tous les livres dans le fichier 'books.txt'
        elif choix == 4:
            reinitialiser_matrice_notation() # permet de réinitialiser le fichier de la matrice de notation avec toutes les valeurs à 0
        elif choix == 5:
            continuer = False # retour au menu principal


#############################
# Corps du programme principal lancé à l'ouverture du programme
if __name__ == '__main__':
    #Initialisation
    debug_fichiers() # permet de reformater les fichiers 'txt' afin d'éviter les bugs par la suite
    recup_fichier_matrice() # recupere la matrice de notation dans le fichier et vérifie qu'elle est bien valide

    continuer = True
    while continuer:  # boucle pour afficher le menu principal en boucle jusqu'à la fermeture du programme
        ## menu principal
        print("      ------ Menu principal ------")
        print("   1 - Profils des lecteurs")
        print("   2 - Visiter le dépôt des livres")
        print("   3 - Recommandation")
        print("   4 - Réinitialiser les données")
        print("   5 - Quitter")
        choix = input("\nPour faire votre choix, entrez 1, 2, 3, 4 ou 5 : ")
        while choix not in {"1", "2", "3", "4", "5"}:  ## Saisie sécurisée
            choix = input("Erreur... " + choix + " n'est pas compris dans 1, 2, 3, 4 ou 5 : ")
        print("\n")

        choix = int(choix)
        if choix == 1:
            menu_profils()  ## lance la fonction de gestion du profils des lecteurs
        elif choix == 2:
            menu_livres()  ## lance la fonction de gestion du dépôt des livres
        elif choix == 3:
            menu_recommandation()  ## lance la fonction de recommandation d'un livre
        elif choix == 4:
            menu_reinitialiser()
        else:
            continuer = False  ## permet de quitter la boucle et fermer le programme


    #Sauvegarde des données avant de quitter (matrice de notation)
    enregistrer_matrice_notation()

    print("      ------ Fin du programme ------")
