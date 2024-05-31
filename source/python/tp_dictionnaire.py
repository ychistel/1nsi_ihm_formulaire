from capitales import capitales

def cle_par_initiale(dico,lettre):
    """
    renvoie la liste des clés du dictionnaire *dico* dont l'initiale *lettre* est donnée en argument
    """
    tableau_cle = []
    for cle in dico:
        if cle[0] == lettre:
            tableau_cle.append(cle)
    return tableau_cle

def valeur_par_initiale(dico,lettre):
    """
    renvoie la liste des valeurs du dictionnaire *dico* dont l'initiale *lettre* est donnée en argument
    """
    tableau_valeur = []
    for valeur in capitales.values():
        if valeur[0] == lettre.upper():
            tableau_valeur.append(valeur)
    return tableau_valeur

def cle_egale_valeur(dico):
    """
    renvoie la liste des clés ou valeurs du dictionnaire *dico* lorsque la clé et la valeur sont égales 
    """
    liste = []
    for item in capitales.items():
        if item[0] == item[1]:
            liste.append(item[0])
    return liste

if __name__ == '__main__':
    print(cle_par_initiale(capitales,'B'))
    print(valeur_par_initiale(capitales,'L'))
    print(cle_egale_valeur(capitales))