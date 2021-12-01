#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#   recommandation.py
#   ==> comporte les fonctions nécessaires à la notation et aux recommandations
#   ==> détails dans le README
#
#   Auteurs: Maël Aubert, Marius Chevailler
#----------------------------------------------------------------------------

from livres import *
from fonctions_generales import *
from math import *
from random import randint

"""FONCTIONS DE NOTATION"""
def ajouter_note(pseudo, num_livre, note):
    #recuperer la position du pseudo
    with open("readers.txt", "r") as f:
        pos_pseudo=0
        for ligne in f:
            if "\n" in ligne:  # permet de retirer les \n a chaque retour à la ligne
                ligne = ligne[:-1]
            if pseudo == ligne.split(", ")[0]:
                break
            pos_pseudo+=1
    #ecrire note en pos_pseudo,num_livre-1
    global matrice_note
    matrice_note[pos_pseudo][num_livre-1]=note

def noter_livre():
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

        var_pos_pseudo=pos_pseudo(pseudo)
        liste_lu=trouver_livres_lu(var_pos_pseudo)
        liste_lu.sort()
        nb_livres=afficher_livres(False,liste_lu)
        # affichage des livres disponibles et récupération du nombre de livres

        # choix des livres lus
        num_livre=input("\n\nEntrez le numéros du livre que vous voulez noter : ")
        while continuer:
            if num_livre.isnumeric()==False or int(num_livre) not in range(1,nb_livres+1):
                num_livre = input("Erreur... Vous devez entrez seulement un nombre entier correspondant à un livre affiché ci-dessus  : ")
            else:
                continuer=False



        num_livre = int(num_livre)

        #choix de la note
        note = input("Entrez une note pour ce livre (entre 1 et 5) : ")
        while note.isnumeric()==False or int(note) not in range(1,6):
            note = input("Erreur... Votre note doit être un entier comprise entre 1 et 5 :")
        note = int(note)
        print("num livre:",num_livre)
        print("liste_lu:",liste_lu)

        print(liste_lu[num_livre-1]+1, note)

        ajouter_note(pseudo, liste_lu[num_livre-1]+1, note)


def afficher_notation():
    for i in range(len(matrice_note)):
        for j in range(len(matrice_note[0])):
            print(matrice_note[i][j], end=' ')
        print("")


def creer_matrice_notation():
    i, j = 0, 0
    with open('books.txt', 'r') as f_books:
        with open('readers.txt', 'r') as f_readers:
            for ligne in f_books:
                i=i+1
            for ligne in f_readers:
                j=j+1

    global matrice_note
    ##crée une matrice avec [nombre de profils] lignes et [nombre de livres] colonnes
    matrice_note = [0] * j
    for k in range(j):
        matrice_note[k]=[0]*i

def modif_matrice_note(choix, element=''):
    global matrice_note
    if choix =='ajout_profil': ## si un profil est ajouté, on ajoute une ligne (initialisée à 0 )à la matrice
        matrice_note.append([0]*len(matrice_note[0]))

    elif choix == 'ajout_livre': ## si un livre est ajouté, on ajoute une colonne (initialisée à 0 )à la matrice
        for i in range(len(matrice_note)):
            matrice_note[i].append(0)

    elif choix == 'suppr_profil':
        M=[]
        for i in range(len(matrice_note)):
            if i!=element:
                M.append(matrice_note[i])
        matrice_note = M

    elif choix == 'suppr_livre':
        M=[]
        print(len(matrice_note[0]))
        for i in range(len(matrice_note)):
            L=[]
            for j in range(len(matrice_note[0])):
                if j!=element:
                    L.append(matrice_note[i][j])
            M.append(L)
        matrice_note=M


"""FONCTIONS DE SIMILARITE"""
def afficher_similarite():
    print("afficher similarités")

def suggerer_livres():
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
        creer_matrice_simi()
        pos_simi=trouver_lecteur_simi(pseudo)
        print(pos_simi)
        livres_lu=trouver_livres_lu(pos_pseudo(pseudo))
        livres_lu_simi=trouver_livres_lu(pos_simi)

        livres_lu_diff=[]
        for val in livres_lu_simi:
            if val not in livres_lu:
                livres_lu_diff.append(val)
        if len(livres_lu_diff)==0:
            print("Nous ne pouvons pas vous recommander de nouveau livres car vous avez lu les mêmes livres...")
        else:
            nb_livres=afficher_livres(False,livres_lu_diff)
            # ajout du livre dans la liste des livres lu
            val = ""
            while val != 0:
                val = input("\n\nEntrez le numéro le numéro d'un livre que vous voulez lire.\nSi vous ne voulez pas en lire, écrivez '0' : ")
                try:
                    val = int(val)
                except ValueError:
                    print("Erreur...\nVous devez entrez seulement un nombre correspondants aux livres affichés ci-dessus  : ")
                else:
                    if val > nb_livres:
                        print("Erreur...\nVous devez entrez seulement un nombre correspondants aux livres affichés ci-dessus  : ")
                    elif val!=0:
                        livres_lu.append(livres_lu_diff[val-1])
                        modifier_livres_lus(pseudo,livres_lu)
                        print(" ✔ liste des livres lu mise à jour\n")
                        val=0

                        """PROPOSER DE NOTER LE LIVRE"""



def creer_matrice_simi():
    """TEMPORAIRE"""
    global matrice_note
    matrice_note=[]
    for i in range(nombre_profils()):
        L=[]
        for j in range(19):
            L.append(randint(0,5))
        matrice_note.append(L)
    """TEMPORAIRE"""

    global matrice_simi
    matrice_simi=[]
    for i in range(nombre_profils()):
        L=[]
        for j in range(nombre_profils()):
            L.append(0)
        matrice_simi.append(L)

    for i in range(nombre_profils()):
        for j in range(nombre_profils()):
            notes1 = matrice_note[i]
            notes2 = matrice_note[j]
            sommenotes1, sommenotes2 = 0, 0
            for k in range(len(notes1)):
                sommenotes1 = sommenotes1 + notes1[k]**2
                sommenotes2 = sommenotes2 + notes2[k]**2
            if i==j:
                matrice_simi[i][j]=1
            elif sommenotes1==0 or sommenotes2==0:
                matrice_simi[i][j]=0
            else:
                N=0
                for k in range(len(notes1)):
                    N=N+notes1[k]*notes2[k]
                D=sqrt(sommenotes1)*sqrt(sommenotes2)
                matrice_simi[i][j]=round(N/D,2)

def trouver_lecteur_simi(pseudo):
    with open('readers.txt','r') as f_readers:
        i=0
        for ligne in f_readers:
            if pseudo == ligne.split(", ")[0]:
                num_ligne=i
            i+=1
    val_max=0
    for i in range(nombre_profils()):
        if i!=num_ligne and val_max<matrice_simi[num_ligne][i]:
            val_max=matrice_simi[num_ligne][i]
            pos_max=i
    return pos_max


