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


def afficher_livres():
    with open("books.txt","r") as f_books:
        i=0
        for ligne in f_books:
            i+=1
            print(i,"-",ligne,end="")
    print("")
    return i
