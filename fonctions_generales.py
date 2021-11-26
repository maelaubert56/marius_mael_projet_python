#ce module accueil toutes les fonctions utilisées par plusieurs modules à la fois (afin d'éviter les erreurs importation circulaires

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
            if pseudo == ligne.split(", ")[0]:
                deja_present = True
                break

    return pseudo, deja_present


def afficher_livres(all=True,pos_livres=[]):
    if all:
        with open("books.txt","r") as f_books:
            i=0
            for ligne in f_books:
                i+=1
                print(i,"-",ligne,end="")
        print("")
        nblivres = i
    else:
        with open("books.txt","r") as f_books:
            i=0
            j=0
            for ligne in f_books:
                if i in pos_livres:
                    j+=1
                    print(j,"-",ligne,end="")
                i += 1
        print("")
        nblivres = j

    return nblivres


def nombre_profils():
    with open("readers.txt", "r") as f_readers:
        i = 0
        for ligne in f_readers:
            i += 1
    return i

def trouver_livres_lu(pos):
    with open('booksread.txt','r') as f_booksread:
        i=0
        liste_lu=[]
        for ligne in f_booksread:
            if i==pos:
                content=ligne[:-1].split(", ")

                for j in range(1,len(content)):
                    liste_lu.append(int(content[j]))
            i+=1
        return liste_lu

def pos_pseudo(pseudo):
    with open('readers.txt', 'r') as f_readers:
        i = 0
        pos=-1
        for ligne in f_readers:
            if ligne.split(", ")[0]==pseudo:
                pos=i
            i += 1
        return pos


def modifier_livres_lus(pseudo,new_liste_booksread):
    with open('booksread.txt', 'r') as f_booksread:  # les livres lus sont contenus dans une nouvelle liste
        liste_booksread = []
        for ligne in f_booksread:
            liste_booksread.append(ligne[:-1])
    with open('booksread.txt','w') as f_booksread:
        for i in range(len(liste_booksread)):  # on modifie le profil souhaité grace à la liste
            if liste_booksread[i].split(", ")[0] == pseudo:
                liste_booksread[i] = pseudo +", "+ ", ".join([str(k) for k in new_liste_booksread])
            liste_booksread[i] = liste_booksread[i] + '\n'  # on rajoute le retour à la ligne à chaque titre
            f_booksread.write(liste_booksread[i])  # on réécrit le fichier grace à la liste crée ulterieurement