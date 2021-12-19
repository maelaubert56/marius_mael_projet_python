#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#   profils.py
#   ==> comporte les fonctions nécessaires à la gestion des profils
#
#   Auteurs: Maël Aubert, Marius Chevailler
# ----------------------------------------------------------------------------
from livres import *
from recommandation import *
from fonctions_generales import *


def questions_profil(): #pose les question necessaires a la création d'un profil, et renvoie 3 nombres correspondant aux choix
    # récolte des informations du profil
    num_genre = input("\n\nQuel est votre genre ?\n  1 <-- HOMME\n  2 <-- FEMME\n  3 <-- PEU IMPORTE\n     : ")
    while num_genre != "1" and num_genre != "2" and num_genre != "3":
        num_genre = (input("    Vous devez entrer la valeur 1, 2 ou 3: "))

    num_age = input(
        "\n\nQuel est votre tranche d'âge ?\n  1 <-- de moins de 18 ans\n  2 <-- de 19 à 25 ans\n  3 <-- plus de 25 ans\n     : ")
    while num_age != "1" and num_age != "2" and num_age != "3":
        num_age = (input("    Vous devez entrer la valeur 1, 2 ou 3: "))

    num_style_lect = input(
        "\n\nQuel est votre style de lecture préféré ?\n  1 <-- Science-fiction\n  2 <-- Biographie\n  3 <-- Horreur\n  4 <-- Romance\n  5 <-- Fable\n  6 <-- Histoire\n  7 <-- Comédie\n     : ")
    while True:
        try:
            int(num_style_lect)
        except ValueError:
            print("    Ceci n'est pas un nombre....")
        else:
            if int(num_style_lect) in range(1, 8):
                break
        num_style_lect = (input("    Entrez un nombre de 1 à 7 : "))
    print("\n\nLivres dans la bibliothèque :\n")
    # Affiche les livres et demande d'entrer les livres lus

    afficher_livres()
    livres_lus = choisir_livre()

    return num_genre, num_age, num_style_lect, livres_lus


def ajout_profil(): # pose les questions nécessaire pour récolter les informations du nouveau profil et les ajoute aux fichiers readers.txt et booksread.txt (propose également de noter un livre)
    # test du pseudo dans le fichier 'readers.txt'
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        pseudo, deja_present = test_pseudo_present()
        continuer = 'n'
        if deja_present:  # si le pseudo existe déjà, on propose de ressaisir ou de quitter
            continuer = input("Ce pseudo existe déjà, voulez vous saisir un autre pseudo ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre pseudo ? o/n ")

    # ajout du profil et des livres lus
    if deja_present == False:
        num_genre, num_age, num_style_lect, livres_lu = questions_profil()
        # ajout des infos dans le fichier "readers.txt"
        with open('readers.txt', 'a') as f_readers:
            f_readers.write(pseudo + ", " + num_genre + ", " + num_age + ", " + num_style_lect + "\n")
        modif_matrice_note('ajout_profil')
        print(" ✔ profil ajouté")

        with open('booksread.txt',
                  'a') as f_booksread:  # ajout des livres lus (si aucun livre lu, seul le pseudo apparaitra)
            f_booksread.write(pseudo + ", " + ", ".join(map(str, livres_lu)) + "\n")

        if len(livres_lu) != 0:  ## si des livres ont été ajoutés : proposition de noter les livres lus
            print(" ✔ liste des livres lu mise à jour\n")

            noter = input("Voulez vous noter les livres que vous avez déja lu ? o/n ")
            while noter not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                noter = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous notez les livres ? o/n ")

            if noter in {'oui', 'Oui', 'O', 'o'}:
                noter_livre(True, pseudo)
                print("\n\n")


def modifier_profil(): #permet de modifier les informations de sexe, d'age, de style de lecture et les livres lus par profil existant
    # On récupère le pseudo du profil à modifier
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        pseudo, deja_present = test_pseudo_present()
        continuer = 'n'
        if deja_present == False:  # si le pseudo existe déjà, on propose de ressaisir ou de quitter
            continuer = input("Ce profil n'existe pas, voulez vous saisir un autre pseudo ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre pseudo ? o/n ")

    if deja_present:  # on demande une confirmation
        continuer = input("Vous allez modifier le profil '" + pseudo + "'. Continuer ? o/n ")
        while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
            continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous continuer ? o/n ")
        if continuer in {'oui', 'Oui', 'O', 'o'}:
            num_genre, num_age, num_style_lect, livres_lu = questions_profil()  # On recupere les nouvelles infos du profil
            with open('readers.txt', 'r') as f_profils:  # les profils sont contenus dans une nouvelle liste
                liste_profils = []
                for ligne in f_profils:
                    liste_profils.append(ligne[:-1])

            with open('readers.txt', 'w') as f_profils:
                for i in range(len(liste_profils)):  # on modifie le livre souhaité grace à la liste
                    if pseudo in liste_profils[i]:
                        liste_profils[i] = pseudo + ",  " + num_genre + ",  " + num_age + ",  " + num_style_lect
                    liste_profils[i] = liste_profils[i] + '\n'  # on rajoute le retour à la ligne à chaque titre
                    f_profils.write(liste_profils[i])  # on réécrit le fichier grace à la liste créé précédement

            with open('booksread.txt', 'r') as f_booksread:  # les lignes de booksread.txt sont contenus dans une liste
                liste_livres_lu = []
                for ligne in f_booksread:
                    liste_livres_lu.append(ligne[:-1])
            with open('booksread.txt', 'w') as f_booksread:
                for i in range(len(liste_livres_lu)):
                    if pseudo == liste_livres_lu[i].split(", ")[
                        0]:  # si on est à la ligne correspondant au pseudo: on la remplace par les nouveaux livres lu
                        liste_livres_lu[i] = pseudo + ", " + ", ".join(map(str, livres_lu))
                    liste_livres_lu[i] = liste_livres_lu[i] + '\n'  # on rajoute le retour à la ligne à chaque titre
                    f_booksread.write(liste_livres_lu[i])  # on ajoute la ligne au fichier booksread.txt
            print(" ✔ profil modifié\n")


def suppr_profil(): #permet de supprimer un profil des fichiers readers.txt, booksread.txt ainsi que de retirer sa ligne dans la matrice de notation
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        pseudo, deja_present = test_pseudo_present()
        continuer = 'n'
        if deja_present == False:  # si le pseudo existe déjà, on propose de ressaisir ou de quitter
            continuer = input("Ce profil n'existe pas, voulez vous saisir un autre pseudo ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre pseudo ? o/n ")
    if deja_present:
        continuer = input("Vous allez supprimer le profil '" + pseudo + "'. Continuer ? o/n ")
        while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
            continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous continuer ? o/n ")
        if continuer in {'oui', 'Oui', 'O', 'o'}:

            with open('readers.txt', 'r') as f_readers:
                liste_readers = []
                i = 0
                for ligne in f_readers:
                    if pseudo != ligne.split(", ")[0]:
                        liste_readers.append(ligne)
                    else:
                        emplacement_suppr = i
                    i += 1
            with open('readers.txt', 'w') as f_readers:
                for i in range(len(liste_readers)):
                    f_readers.write(liste_readers[i])

            with open('booksread.txt', 'r') as f_booksread:
                liste_booksread = []
                for ligne in f_booksread:
                    if pseudo != ligne.split(", ")[0]:
                        liste_booksread.append(ligne)
            with open('booksread.txt', 'w') as f_booksread:
                for i in range(len(liste_booksread)):
                    f_booksread.write(liste_booksread[i])
            modif_matrice_note('suppr_profil', emplacement_suppr)
            print(" ✔ profil supprimé\n")


def voir_profil(): #permet d'afficher les données d'un profil (sexe, age, style de lecture)
    genre = ["Homme", "Femme", "Peu importe"]
    age = ["≤ 18 ans", "Entre 18 ans et 25 ans", "Plus de 25 ans"]
    style_de_lecture = ["Science-fiction", "Biographie", "Horreur", "Romance", "Fable", "Histoire", "Comédie"]
    continuer = 'o'
    deja_present = False
    while continuer in {'oui', 'Oui', 'O', 'o'}:
        pseudo, deja_present = test_pseudo_present()
        continuer = 'n'
        if deja_present == False:  # si le pseudo existe déjà, on propose de ressaisir ou de quitter
            continuer = input("Ce profil n'existe pas, voulez vous saisir un autre pseudo ? o/n ")
            while continuer not in {'oui', 'Oui', 'O', 'o', 'non', 'Non', 'N', 'n'}:
                continuer = input("Vous devez répondre 'o' ou 'n'...\nVoulez vous saisir un autre pseudo ? o/n ")
    if deja_present:
        with open('readers.txt', 'r') as f_readers:
            for ligne in f_readers:
                data_profil = ligne[:-1].split(", ")
                if pseudo == data_profil[0]:
                    data_profil = ligne.split(", ")
                    print("     ----  Affichage du profil ----")
                    print("          Pseudo :", data_profil[0])
                    print("           Genre :", genre[int(data_profil[1]) - 1])
                    print("             Age :", age[int(data_profil[2]) - 1])
                    print("Style de lecture :", style_de_lecture[int(data_profil[3]) - 1] + "\n")
