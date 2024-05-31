from random import choice

def choisir_pays(dico):
    un_pays = choice(list(dico.keys()))    
    return un_pays

def choisir_capitale(dico):
    une_capitale = choice(list(dico.values()))
    return une_capitale

def questionnaire(dico):
    pays = choisir_pays(dico)
    villes_reponses = []
    villes_reponses.append(dico[pays])
    villes_reponses.append(choisir_capitale(dico))
    villes_reponses.append(choisir_capitale(dico))
    villes_reponses.sort()
    return {'pays':pays,'rep0':villes_reponses[0],'rep1':villes_reponses[1],'rep2':villes_reponses[2]}

def verifier(dico,cle,valeur):
    if cle == '' or valeur == '':
        return False
    else:
        return dico[cle] == valeur
