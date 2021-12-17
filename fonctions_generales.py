#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#   fonctions_generales.py
#   ==> accueil toutes les fonctions utilisées par plusieurs modules à la fois (afin d'éviter les erreurs importation circulaires)
#   ==> détails dans le README
#
#   Auteurs: Maël Aubert, Marius Chevailler
# ----------------------------------------------------------------------------

def debug_fichiers(): # permet de reformater les fichiers 'txt' afin qu'ils soient lisible par le programme sans bug
    with open('booksread.txt','r') as f_booksread:
        tab_livres_lu=[]
        for ligne in f_booksread:
            liste_livres_lu=[]
            ligne=ligne[:-1].split(", ")
            liste_livres_lu.append(ligne[0])
            nblignes=nombreDeLignes("books.txt")
            for i in range(1,len(ligne)):
                ligne[i]=int(ligne[i])
                if ligne[i] in range(1,nblignes+1) and (str(ligne[i]) not in liste_livres_lu): # on ajoute la valeur seulement si la valeur est >0 et qu'elle n'est pas déja présente
                    liste_livres_lu.append(str(ligne[i]))
            tab_livres_lu.append(liste_livres_lu)

    with open('booksread.txt','w') as f_booksread: # On réécrit le fichier avec les bonnes valeurs
        for i in range(len(tab_livres_lu)):
            f_booksread.write(", ".join(tab_livres_lu[i])+"\n")

def reinitialiser(element=""):
    if element == "profils":
        with open("readers.txt","w") as f_profils:
            f_profils.write("")
        with open("booksread.txt", "w") as f_booksread:
            f_booksread.write("")

    elif element == "lectures":
        with open("booksread.txt","r") as f_booksread:
            liste_pseudo=[]
            for ligne in f_booksread:
                liste_pseudo.append(ligne.split(", ")[0])
        with open("booksread.txt","w") as f_booksread:
            for pseudo in liste_pseudo:
                f_booksread.write(pseudo+",\n")

    elif element == "livres":
        with open("books.txt", "w") as f_books:
            f_books.write("")

    elif element == "notes":
        with open("matrice_notation.txt", "w") as f_matrice:
            f_matrice.write("")


def choix_pseudo(): #demande d'entrer un pseudo, avec une saisie sécurisé (20 caractères max)
    pseudo = input("Entrez un pseudo de 20 caractères maximum : ")
    while (len(pseudo) not in range(1, 21)) or (" " in pseudo) or ("," in pseudo):
        pseudo = input("Ce pseudo n'est pas valable : ")
    return pseudo


def test_pseudo_present():  # vérifie si un pseudo existe dans readers.txt
    pseudo=choix_pseudo()
    # on vérifie si le pseudo existe déjà
    deja_present = False
    with open("readers.txt", "r") as f:
        for ligne in f:
            if "\n" in ligne:  # permet de retirer les \n a chaque retour à la ligne
                ligne = ligne[:-1]
            if pseudo == ligne.split(", ")[0]:
                deja_present = True  # si le pseudo est présent, deja present est Vrai
                break
    return pseudo, deja_present  # retourne pseudo(str) et deja_present(booléen)


def trouver_livres_lu(pos):
    with open('booksread.txt', 'r') as f_booksread:
        i = 0
        liste_lu = []
        for ligne in f_booksread:
            if i == pos:
                content = ligne[:-1].split(", ")
                for j in range(1, len(content)):
                    liste_lu.append(int(content[j]))
            i += 1
        return liste_lu

def nombreDeLignes(fichier):
    with open(fichier, "r") as f:
        i = 0
        for ligne in f:
            i += 1
    return i

def pos_pseudo(pseudo):
    with open('readers.txt', 'r') as f_readers:
        i = 0
        pos = -1
        for ligne in f_readers:
            if ligne.split(", ")[0] == pseudo:
                pos = i
            i += 1
        return pos

def pos_livre(livre):
    with open('books.txt', 'r') as f_books:
        i = 0
        pos = -1
        for ligne in f_books:
            i += 1
            if ligne == livre:
                pos = i
        return pos


def afficher_livres(all=True,pos_livres=[]):  # permet d'afficher les livres presents dans books.txt (soit tout, soit une liste définie)
    if all:  # on affiche tous les livres avec un numéro devant pour une sélection
        with open("books.txt", "r") as f_books:
            i = 0
            for ligne in f_books:
                i += 1
                print(i, "-", ligne, end="")
        print("")

    else:  # on affiche seulement les livres selon pos_livres avec un numéro devant pour une sélection
        with open("books.txt", "r") as f_books:
            i = 1
            j=1
            for ligne in f_books:
                if i in pos_livres:
                    print(j, "-", ligne, end="")
                    j+=1
                i += 1
        print("")

def choisir_livre(liste_livres=list(range(1,nombreDeLignes("books.txt")+1))):
    nb_livres = len(liste_livres)
    print("\n\nEntrez les numéros des livres que vous avez lus et faites entrer à chaque nouveau livre.\nLorsque vous avez fini ou si vous n'avez rien lu, écrivez '0' : ")
    val = ''
    livres_lus=[]
    while val != 0:
        val = input("-")
        try:
            val = int(val)
        except ValueError:
            print("Erreur...\nVous devez entrez seulement des nombres correspondants aux livres affichés ci-dessus  : ")
        else:
            if val not in range(nb_livres + 1):
                print("Erreur...\nVous devez entrez seulement des nombres correspondants aux livres affichés ci-dessus  : ")
            elif val in livres_lus:
                print("Erreur...\n Vous avez déja entré ce numéro : ")
            elif val != 0:
                livres_lus.append(val)

    for i in range(len(livres_lus)): # on transpose les valeurs récupéré aux emplacements réels des livres dans le fichier
        livres_lus[i]=liste_livres[livres_lus[i]-1]
    return livres_lus

def modifier_livres_lus(pseudo, new_liste_booksread):
    with open('booksread.txt', 'r') as f_booksread:  # les livres lus sont contenus dans une nouvelle liste
        liste_booksread = []
        for ligne in f_booksread:
            liste_booksread.append(ligne[:-1])
    with open('booksread.txt', 'w') as f_booksread:
        for i in range(len(liste_booksread)):  # on modifie le profil souhaité grace à la liste
            if liste_booksread[i].split(", ")[0] == pseudo:
                liste_booksread[i] = pseudo + ", " + ", ".join([str(k + 1) for k in new_liste_booksread])
            liste_booksread[i] = liste_booksread[i] + '\n'  # on rajoute le retour à la ligne à chaque titre
            f_booksread.write(liste_booksread[i])  # on réécrit le fichier grace à la liste crée ulterieurement

