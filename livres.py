#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#   livres.py
#   ==> comporte les fonctions nécessaires à la gestion des livres
#   ==> détails dans le README
#
#   Auteurs: Maël Aubert, Marius Chevailler
# ----------------------------------------------------------------------------

from recommandation import *
from fonctions_generales import *


def test_livre():  # vérifie si un livre existe dans book.txt
    nom_livre = input("Entrez le nom du livre: ")
    while len(nom_livre) != 0 and nom_livre == " ":
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


def ajout_livre():  # permet d'ajouter un livre à books.txt
    ## Récupération du nom du livre
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        nom_livre, deja_present = test_livre()  # on vérifie que le livre n'existe pas déja
        continuer = 'n'
        if deja_present:  # si le livre existe déjà, on propose de ressaisir ou de quitter
            continuer = input("Ce livre existe déjà, voulez vous saisir un autre titre de livre ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre  ? o/n ")
    ## Ajout du livre dans le fichier books.txt
    if deja_present == False:
        with open('books.txt', 'a') as f_books:
            f_books.write(nom_livre + "\n")

        modif_matrice_note('ajout_profil')  # on ajoute une colonne à la matrice de notation
        print(" ✔ livre ajouté\n")

def modifier_livre():  # permet de modifier le titre d'un livre existant dans books.txt
    ## Récupération du nom du livre
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        nom_livre, deja_present = test_livre()  # On vérifie  que le livre est présent dans books.txt
        continuer = 'n'
        if deja_present == False:  # si le livre n'existe pas, on propose de ressaisir ou de quitter
            continuer = input("Ce livre n'existe pas, voulez vous saisir un autre titre de livre ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input(
                    "Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre titre de livre ? o/n ")
    if deja_present:  # Si le livre est présent, on demande le nouveau nom (si il est different de l'ancien)
        continuer = input("Vous allez modifier le livre '" + nom_livre + "'. Continuer ? o/n ")
        while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
            continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous continuer ? o/n ")
        if continuer in {'oui', 'Oui', 'O', 'o'}:
            new_titre = input("Veuillez saisir un nouveau titre pour ce livre :")
            while new_titre == nom_livre:
                print("Vous n'avez pas apporté de modifications")
                new_titre = input("Veuillez saisir un nouveau titre pour ce livre :")

            ## Modification du livre dans le ficher books.txt
            with open('books.txt', 'r') as f_books:  # les livres sont contenus dans une liste
                liste_books = []
                for ligne in f_books:
                    liste_books.append(ligne[:-1])
            with open('books.txt', 'w') as f_books:
                for i in range(len(liste_books)):  # on modifie le livre souhaité dans la liste
                    if liste_books[i] == nom_livre:
                        liste_books[i] = new_titre
                    liste_books[i] = liste_books[i] + '\n'  # on rajoute le retour à la ligne à chaque titre
                    f_books.write(liste_books[i])  # on réécrit le fichier grace à la liste crée précedemment
            print(" ✔ livre modifié\n")

def supprimer_livre():  # permet de supprimer un livre dans books.txt et booksread.txt
    ## Récupération du nom du livre
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
        continuer = input("Vous allez supprimer le livre '" + nom_livre + "'. Continuer ? o/n ")
        while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
            continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous continuer ? o/n ")
        if continuer in {'oui', 'Oui', 'O', 'o'}:

            ## Suppression du livre
            with open('books.txt', 'r') as f_books:
                liste_books = []
                i = 0
                for ligne in f_books:
                    if nom_livre != ligne[:-1]:  # On ajoute les livres a une liste (sauf le livre à supprimer)
                        liste_books.append(ligne)
                    else:
                        emplacement_suppr = i+1  # On récupère l'emplacement de suppression pour supprimer son apparition dans d'autres fichiers
                    i += 1
            with open('books.txt', 'w') as f_books:  # on réécrit le fichier sans le livre à supprimer
                for i in range(len(liste_books)):
                    f_books.write(liste_books[i])
            modif_matrice_note('suppr_livre',emplacement_suppr)  # on retire la colonne correspondant au livre supprimé dans la matrice de notation

            # on supprime les apparition du livre supprimé dans booksread, et on décale les positions suivantes
            with open("booksread.txt","r") as f_booksread:
                newliste=[]
                for ligne in f_booksread:
                    newligne=ligne[:-1].split(", ")
                    i=1
                    while i in range(1,len(newligne)):
                        newligne[i] = int(newligne[i])
                        if newligne[i]==emplacement_suppr:
                            del newligne[i]
                            i-=1
                        elif newligne[i]>emplacement_suppr:
                            newligne[i]=newligne[i]-1
                        i+=1
                    newliste.append(newligne)

            with open('booksread.txt','w') as f_booksread:  # ajout des livres lus (si aucun livre lu, seul le pseudo apparaitra)
                for i in range(len(newliste)):
                    f_booksread.write(", ".join(list(map(str,newliste[i]))) + "\n")

            print(" ✔ livre supprimé\n")


def trouver_livre_non_lus(pseudo): # retourne une liste des livres non lus par le {pseudo}
    ensemble_livres = set(list(range(1,nombreDeLignes("books.txt")+1)))
    ensemble_livres_lus = set(trouver_livres_lu(pos_pseudo(pseudo)))
    print(list(ensemble_livres-ensemble_livres_lus))
    return list(ensemble_livres-ensemble_livres_lus)# on retire l'ensemble des livres lus à l'ensemble des livres existantes (tous les chiffres de 1 au nombre de livres)

def lire_livre():
    # on recupère le pseudo et on vérifie qu'il existe
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
        livres_non_lus=trouver_livre_non_lus(pseudo)
        afficher_livres(False,livres_non_lus)
        ajouter_livres_lus(pseudo,choisir_livre(livres_non_lus))

def ajouter_livres_lus(pseudo, nouveaux_livres_lus):
    with open('booksread.txt', 'r') as f_booksread:  # les livres lus sont contenus dans une nouvelle liste
        liste_booksread = []
        for ligne in f_booksread:
            liste_booksread.append(ligne[:-1])
    with open('booksread.txt', 'w') as f_booksread:
        for i in range(len(liste_booksread)):  # on modifie le profil souhaité grace à la liste
            if liste_booksread[i].split(", ")[0] == pseudo:
                liste_booksread[i] = liste_booksread[i] +", "+ ", ".join(map(str,nouveaux_livres_lus))
            f_booksread.write(liste_booksread[i]+ '\n')  # on réécrit le fichier grace à la liste crée ulterieurement + un retour a la ligne à chaque ligne

