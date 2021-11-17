
def noter_livre():
    print("noter livre")

def suggerer_livres():
    print("suggerer livre")

def afficher_notation():
    print(matrice_note)

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
    matrice_note = [[0]*i]*j ##crée une matrice avec [nombre de profils] lignes et [nombre de livres] colonnes

def modif_matrice_note(choix, element=''):
    print(element)

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
        print(matrice_note)

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
        print(matrice_note)


