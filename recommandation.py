
def noter_livre():
    print("noter livre")

def suggerer_livres():
    print("suggerer livre")

def afficher_notation():
    print("afficher notation")

def afficher_similarite():
    print("afficher similarités")

def creer_matrice_notation():
    i=0
    j=0
    with open('books.txt', 'r') as f_books:
        with open('readers.txt', 'r') as f_readers:
            for ligne in f_books:
                i=i+1
            for ligne in f_readers:
                j=j+1
    M = []
    for k in range(j):
        L = []
        for l in range(i):
            L.append(0)
        M.append(L)
    print(M)