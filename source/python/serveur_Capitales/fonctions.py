from random import choice

def choisir_pays(dico):
    """
    la fonction renvoie un pays choisi aléatoirement parmi les pays du dictionnaire capitales passé en argument.
    la fonction choice renvoie une valeur prise au hasard dans un tableau.
    """
    pass

def choisir_capitale(dico):
    """
    la fonction renvoie une capitale choisie aléatoirement parmi les capitales du dictionnaire capitales passé en argument.
    la fonction choice renvoie une valeur prise au hasard dans un tableau.
    """
    pass

def verifier(dico,cle,valeur):
    """
    la fonction renvoie un booléen.
    - True si la "valeur" passée en argument est bien associée à la "clé" passée en argument dans le dictionnaire "dico" passé en argument.
    - False dans le cas contraire.
    """
    pass

def questionnaire(dico):
    """
    le code ci-dessous est à modifier et compléter pour que le pays et les villes soient choisies au hasard !
    - pays est une chaine de caractère dont la valeur est un pays choisi aléatoirement dans le dictionnaire "capitales"
    - villes_reponses est un tableau qui contient 3 capitales dont la bonne réponse et 2 villes choisies aléatoirement dans le dictionnaire "capitales".
    la fonction renvoie un dictionnaire contenant un pays et 3 capitales. Les clés du dictionnaire sont 'pays', 'rep0', 'rep1', et 'rep2' et ne sont pas modifiables.
    """
    pays = 'France'
    villes_reponses = ['Paris','Londres','Rome']

    # Cette dernière ligne ne doit pas être modifiée
    return {'pays':pays,'rep0':villes_reponses[0],'rep1':villes_reponses[1],'rep2':villes_reponses[2]}
