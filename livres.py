#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#   livres.py
#   ==> comporte les fonctions nécessaires à la gestion des livres
#   ==> détails dans le README
#
#   Auteurs: Maël Aubert, Marius Chevailler
#----------------------------------------------------------------------------
from recommandation import *


def afficher_livres():
    with open("books.txt","r") as f_books:
        i=0
        for ligne in f_books:
            i+=1
            print(i,"-",ligne,end="")
    print("")
    return i

def ajout_livre() :
    # test du livre dans le fichier 'books.txt'
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        nom_livre, deja_present = test_livre()
        continuer = 'n'
        if deja_present:  # si le livre existe déjà, on propose de ressaisir ou de quitter
            continuer = input("Ce livre existe déjà, voulez vous saisir un autre titre de livre ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre  ? o/n ")
    # ajout du profil et des livres lus
    if deja_present == False:
        # ajout du livre dans le fichier "books.txt"
        with open('books.txt', 'a') as f_books:
            f_books.write(nom_livre + "\n")
        modif_matrice_note('ajout_profil')
        print(" ✔ livre ajouté\n")

def modifier_livre() :
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        nom_livre, deja_present = test_livre()
        continuer = 'n'
        if deja_present == False:  # si le livre n'existe pas, on propose de ressaisir ou de quitter
            continuer = input("Ce livre n'existe pas, voulez vous saisir un autre titre de livre ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input(
                    "Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre titre de livre ? o/n ")
    if deja_present:
        continuer = input("Vous allez modifier le livre '" + nom_livre + "'. Continuer ? o/n ")
        while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
            continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous continuer ? o/n ")
        if continuer in {'oui', 'Oui', 'O', 'o'}:
            new_titre=input("Veuillez saisir un nouveau titre pour ce livre :")
            while new_titre==nom_livre :
                print("Vous n'avez pas apporté de modifications")
                new_titre = input("Veuillez saisir un nouveau titre pour ce livre :")


            with open('books.txt', 'r') as f_books:  # les livres  sont contenus dans une nouvelle liste
                liste_books = []
                for ligne in f_books:
                        liste_books.append(ligne[:-1])
            with open('books.txt',
                      'w') as f_books:
                for i in range(len(liste_books)): # on modifie le livre souhaité grace à la liste
                    if liste_books[i]==nom_livre:
                        liste_books[i]=new_titre
                    liste_books[i]=liste_books[i]+'\n' # on rajoute le retour à la ligne à chaque titre
                    f_books.write(liste_books[i]) # on réécrit le fichier grace à la liste crée ulterieurement
            print(" ✔ livre modifié\n")

def supprimer_livre() :
        continuer = 'o'
        deja_present = False
        while continuer in {'oui', 'Oui', 'O', 'o'}:
            nom_livre, deja_present = test_livre()
            continuer = 'n'
            if deja_present == False:  # si le livre n'existe pas, on propose de ressaisir ou de quitter
                continuer = input("Ce livre n'existe pas, voulez vous saisir un autre titre de livre ? o/n ")
                while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                    continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre titre de livre ? o/n ")
        if deja_present:
            continuer = input("Vous allez supprimer le livre '" + nom_livre + "'. Continuer ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous continuer ? o/n ")
            if continuer in {'oui', 'Oui', 'O', 'o'}:

                with open('books.txt', 'r') as f_books: #les livres désirables sont contenus dans une nouvelle liste
                    liste_books = []
                    i=0
                    for ligne in f_books:
                        if nom_livre != ligne[:-1]: # on exclut le \n présent sur chaque ligne du fichier dans la comparaison avec le titre du livre.
                            liste_books.append(ligne)
                        else:
                            emplacement_suppr = i
                        i+=1
                with open('books.txt', 'w') as f_books: # on réécrit le fichier sans le livre indésirable grace à la liste crées ulterieurement.
                    for i in range(len(liste_books)):
                        f_books.write(liste_books[i])
                modif_matrice_note('suppr_livre', emplacement_suppr)
                print(" ✔ livre supprimé\n")


def test_livre():
    # on limite le pseudo à 20 caractère
    nom_livre = input("Entrez le nom du livre: ")
    while nom_livre==" ":
        nom_livre = input("Ce nom de livre n'est pas valable : ")

    # on vérifie si le livre existe déjà
    deja_present = False
    with open("books.txt", "r") as f:
        for ligne in f:
            if "\n" in ligne:  # permet de retirer les \n a chaque retour à la ligne
                ligne = ligne[:-1]
            if nom_livre == ligne:
                deja_present = True
                break

    return nom_livre, deja_present