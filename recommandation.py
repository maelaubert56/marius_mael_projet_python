from livres import *
from fonctions_generales import *


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

        afficher_livres()
        # affichage des livres disponibles et récupération du nombre de livres
        nb_livres = afficher_livres()

        # choix des livres lus
        num_livre=input("\n\nEntrez le numéros du livre que vous voulez noter : ")
        while num_livre.isnumeric()==False or int(num_livre) not in range(1,nb_livres+1):
            num_livre = input("Erreur... Vous devez entrez seulement un nombre entier correspondant à un livre affiché ci-dessus  : ")
        num_livre = int(num_livre)

        #choix de la note
        note = input("Entrez une note pour ce livre (entre 1 et 5) : ")
        while note.isnumeric()==False or int(note) not in range(1,6):
            note = input("Erreur... Votre note doit être un entier comprise entre 1 et 5 :")
        note = int(note)

        ajouter_note(pseudo, num_livre, note)


def suggerer_livres():
    print("suggerer livre")

def afficher_notation():
    for i in range(len(matrice_note)):
        for j in range(len(matrice_note[0])):
            print(matrice_note[i][j], end=' ')
        print("")

def afficher_similarite():
    print("afficher similarités")

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


