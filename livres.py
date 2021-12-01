#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#   livres.py
#   ==> comporte les fonctions nécessaires à la gestion des livres
#   ==> détails dans le README
#
#   Auteurs: Maël Aubert, Marius Chevailler
#----------------------------------------------------------------------------

from recommandation import *
from fonctions_generales import *

def ajout_livre() : # permet d'ajouter un livre à books.txt
    ## Récupération du nom du livre
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        nom_livre, deja_present = test_livre() # on vérifie que le livre n'existe pas déja
        continuer = 'n'
        if deja_present:  # si le livre existe déjà, on propose de ressaisir ou de quitter
            continuer = input("Ce livre existe déjà, voulez vous saisir un autre titre de livre ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre  ? o/n ")
    ## Ajout du livre dans le fichier books.txt
    if deja_present == False:
        with open('books.txt', 'a') as f_books:
            f_books.write(nom_livre + "\n")

        modif_matrice_note('ajout_profil') # on ajoute une colonne à la matrice de notation
        print(" ✔ livre ajouté\n")



def modifier_livre() : # permet de modifier le titre d'un livre existant dans books.txt
    ## Récupération du nom du livre
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        nom_livre, deja_present = test_livre() # On vérifie  que le livre est présent dans books.txt
        continuer = 'n'
        if deja_present == False:  # si le livre n'existe pas, on propose de ressaisir ou de quitter
            continuer = input("Ce livre n'existe pas, voulez vous saisir un autre titre de livre ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input(
                    "Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre titre de livre ? o/n ")
    if deja_present: #Si le livre est présent, on demande le nouveau nom (si il est different de l'ancien)
        continuer = input("Vous allez modifier le livre '" + nom_livre + "'. Continuer ? o/n ")
        while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
            continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous continuer ? o/n ")
        if continuer in {'oui', 'Oui', 'O', 'o'}:
            new_titre=input("Veuillez saisir un nouveau titre pour ce livre :")
            while new_titre==nom_livre :
                print("Vous n'avez pas apporté de modifications")
                new_titre = input("Veuillez saisir un nouveau titre pour ce livre :")

    ## Modification du livre dans le ficher books.txt
            with open('books.txt', 'r') as f_books:  # les livres sont contenus dans une liste
                liste_books = []
                for ligne in f_books:
                        liste_books.append(ligne[:-1])
            with open('books.txt','w') as f_books:
                for i in range(len(liste_books)): # on modifie le livre souhaité dans la liste
                    if liste_books[i]==nom_livre:
                        liste_books[i]=new_titre
                    liste_books[i]=liste_books[i]+'\n' # on rajoute le retour à la ligne à chaque titre
                    f_books.write(liste_books[i]) # on réécrit le fichier grace à la liste crée précedemment
            print(" ✔ livre modifié\n")

def supprimer_livre() : # permet de supprimer un livre dans books.txt et booksread.txt
    ## Récupération du nom du livre
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

    ## Suppression du livre
                with open('books.txt', 'r') as f_books:
                    liste_books = []
                    i=0
                    for ligne in f_books:
                        if nom_livre != ligne[:-1]: # On ajoute les livres a une liste (sauf le livre à supprimer)
                            liste_books.append(ligne)
                        else:
                            emplacement_suppr = i # On récupère l'emplacement de suppression pour supprier son apparition dans d'autres fichiers
                        i+=1
                with open('books.txt', 'w') as f_books: # on réécrit le fichier sans le livre à supprimer
                    for i in range(len(liste_books)):
                        f_books.write(liste_books[i])
                modif_matrice_note('suppr_livre', emplacement_suppr)  # on retire la colonne correspondant au livre supprimé dans la matrice de notation
        #### TODO: FONCTION POUR DECALER TOUS LES CHIFFRES SUPRERIEURS A CE LIVRE DANS booksread.txt  ####
                print(" ✔ livre supprimé\n")


def test_livre(): # vérifie si un livre existe dans book.txt
    nom_livre = input("Entrez le nom du livre: ")
    while len(nom_livre)!=0 and nom_livre==" ":
        nom_livre = input("Ce nom de livre n'est pas valable : ")

    # on vérifie si le livre existe dans books.txt
    deja_present = False
    with open("books.txt", "r") as f:
        for ligne in f:
            if "\n" in ligne:  # permet de retirer les \n a chaque retour à la ligne
                ligne = ligne[:-1]
            if nom_livre == ligne:
                deja_present = True
                break

    return nom_livre, deja_present

