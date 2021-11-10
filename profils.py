#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#   profils.py
#   ==> comporte les fonctions nécessaires à la gestion des profils
#   ==> détails dans le README
#
#   Auteurs: Maël Aubert, Marius Chevailler
#----------------------------------------------------------------------------

from livres import *

def test_pseudo():
    # on limite le pseudo à 20 caractère
    pseudo = input("Entrez un pseudo de 20 caractères maximum : ")
    while len(pseudo) not in range(1, 21):
        pseudo = input("Ce pseudo n'est pas valable : ")

    # on vérifie si le pseudo existe déjà
    deja_present = False
    with open("readers.txt", "r") as f:
        for ligne in f:
            if "\n" in ligne:  # permet de retirer les \n a chaque retour à la ligne
                ligne = ligne[:-1]
            readers_data = ligne.split(", ")
            if pseudo == readers_data[0]:
                deja_present = True
                break

    return pseudo, readers_data, deja_present


def ajout_profil():
    # test du pseudo dans le fichier 'readers.txt'
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        pseudo, deja_present = test_pseudo()
        continuer= 'n'
        if deja_present:  # si le pseudo existe déjà, on propose de ressaisir ou de quitter
            continuer = input("Ce pseudo existe déjà, voulez vous saisir un autre pseudo ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre pseudo ? o/n ")
    # ajout du profil et des livres lus
    if deja_present == False:
        # récolte des informations du profil
        num_genre = input("\n\nQuel est votre genre ?\n  1 <-- HOMME\n  2 <-- FEMME\n  3 <-- PEU IMPORTE\n     : ")
        while num_genre != "1" and num_genre != "2" and num_genre != "3":
            num_genre = (input("    Vous devez entrer la valeur 1, 2 ou 3: "))

        num_age = input("\n\nQuel est votre tranche d'âge ?\n  1 <-- de moins de 18 ans\n  2 <-- de 19 à 25 ans\n  3 <-- plus de 25 ans\n     : ")
        while num_age != "1" and num_age != "2" and num_age != "3":
            num_age = (input("    Vous devez entrer la valeur 1, 2 ou 3: "))

        num_style_lect = input("\n\nQuel est votre style de lecture préféré ?\n  1 <-- Science-fiction\n  2 <-- Biographie\n  3 <-- Horreur\n  4 <-- Romance\n  5 <-- Fable\n  6 <-- Histoire\n  7 <-- Comédie\n     : ")
        while True:
            try:
                int(num_style_lect)
            except ValueError:
                print("    Ceci n'est pas un nombre....")
            else:
                if int(num_style_lect) in range(1, 8):
                    break
            num_style_lect = (input("    Entrez un nombre de 1 à 7 : "))
         # ajout des infos dans le fichier "readers.txt"
        with open('readers.txt', 'a') as f_readers:
            f_readers.write(pseudo + ",  " + num_genre + ",  " + num_age + ",  " + num_style_lect + "\n")

        # affichage des livres disponibles et récupération du nombre de livres
        nb_livres=afficher_livres()

        # choix des livres lus
        print("\n\nEntrez les numéros des livres déjà lus et entrez à chaque nouveau livre.\nLorsque vous avez fini ou si vous n'avez rien lu, écrivez '0' : ")
        val = ""
        livres_lus = []
        while val != 0:
            val = input("- ")
            try:
                val = int(val)
            except ValueError:
                print("Erreur...\nVous devez entrez seulement des nombres correspondants aux livres affichés ci-dessus  : ")
            else:
                if val > nb_livres:
                    print("Erreur...\nVous devez entrez seulement des nombres correspondants aux livres affichés ci-dessus  : ")
                elif val != 0:
                    livres_lus.append(str(val))
        with open('booksread.txt', 'a') as f_booksread:
            f_booksread.write(pseudo+", " + ", ".join(livres_lus) + "\n")

        print(" ✔ profil ajouté\n")

def suppr_profil():
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        pseudo, deja_present = test_pseudo()
        continuer = 'n'
        if deja_present == False:  # si le pseudo existe déjà, on propose de ressaisir ou de quitter
            continuer = input("Ce profil n'existe pas, voulez vous saisir un autre pseudo ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre pseudo ? o/n ")
    if deja_present:
        continuer=input("Vous allez supprimer le profil '"+pseudo+"'. Continuer ? o/n ")
        while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
            continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous continuer ? o/n ")
        if continuer in {'oui', 'Oui', 'O', 'o'}:
            with open('readers.txt', 'w') as f_readers:
                for ligne in f_readers:
                    if pseudo in ligne

def voir_profil():
    genre = ["Homme", "Femme", "Peu importe"]
    age = ["≤ 18 ans", "Entre 18 ans et 25 ans", "Plus de 25 ans"]
    style_de_lecture = ["Science-fiction", "Biographie", "Horreur", "Romance", "Fable", "Histoire", "Comédie"]
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        pseudo, deja_present = test_pseudo()
        continuer= 'n'
        if deja_present==False:  # si le pseudo existe déjà, on propose de ressaisir ou de quitter
            continuer = input("Ce profil n'existe pas, voulez vous saisir un autre pseudo ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre pseudo ? o/n ")
    if deja_present:
        with open('readers.txt','r') as f_readers:
            for ligne in f_readers:
                if pseudo in ligne:
                    if "\n" in ligne:  # permet de retirer les \n a chaque retour à la ligne
                        ligne = ligne[:-1]
                    data_profil= ligne.split(", ")
                    print("     ----  Affichage du profil ----")
                    print("          Pseudo :",data_profil[0])
                    print("           Genre :",genre[int(data_profil[1])])
                    print("             Age :",age[int(data_profil[2])])
                    print("Style de lecture :",style_de_lecture[int(data_profil[3])])