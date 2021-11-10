#!/usr/bin/env python3  Line 1
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#   livres.py
#   ==> comporte les fonctions nécessaires à la gestion des livres
#   ==> détails dans le README
#
#   Auteurs: Maël Aubert, Marius Chevailler
#----------------------------------------------------------------------------

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

        print(" ✔ livre ajouté\n")

def modifier_livre() :
    with open("books.txt", "r") as f_books:
        print("temporaire")

def supprimer_livre() :
    with open("books.txt", "r") as f_books:
        print("temporaire")


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