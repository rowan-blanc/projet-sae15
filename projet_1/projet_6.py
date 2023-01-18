import pandas as pd
mesCours = pd.read_csv("ADECal.csv", encoding='latin-1', delimiter=";", index_col=6)

def choixGroupe(mesCours):
    """Demande à l'utilisateur de choisir son groupe.
    Renvoie aussi le groupe auquel appartient le TP choisi."""
    choixGroupe = str(input("Quel est votre groupe (TDA, TDB, TP1, TP2, TP3, TP4) :"))
    if choixGroupe == "TP1" or choixGroupe == "TP2":
        print("Vous appartennez aussi au TDA")
    elif choixGroupe == "TP3" or choixGroupe == "TP4":
        print("Vous appartennez aussi au TDB")
    return choixGroupe

choixGroupe = choixGroupe(mesCours)
print(choixGroupe)

def modules(mesCours):
    """Renvoie les éléments en fonction du groupe choisi du tableau mesCours.
    En affichant les modules, l'heure de départ et l'heure de fin du cours. """
    if choixGroupe == "TDA":
        groupe = mesCours.loc[[" 1A ", " 1ATDA "], ["Modules", "HStart", "HEnd"]]
        return groupe
    elif choixGroupe == "TDB":
        groupe = mesCours.loc[[" 1A ", " 1ATDB "], ["Modules", "HStart", "HEnd"]]
        return groupe
    elif choixGroupe == "TP1":
        groupe = mesCours.loc[[" 1A ", " 1ATDA ", " 1ATP1 "], ["Modules", "HStart", "HEnd"]]
        return groupe
    elif choixGroupe == "TP2":
        groupe = mesCours.loc[[" 1A ", " 1ATDA ", " 1ATP2 "], ["Modules", "HStart", "HEnd"]]
        return groupe
    elif choixGroupe == "TP3":
        groupe = mesCours.loc[[" 1A ", " 1ATDB ", " 1ATP3 "], ["Modules", "HStart", "HEnd"]]
        return groupe
    elif choixGroupe == "TP4":
        groupe = mesCours.loc[[" 1A ", " 1ATDB ", " 1ATP4 "], ["Modules", "HStart", "HEnd"]]
        return groupe

groupe = modules(mesCours)
print(groupe)