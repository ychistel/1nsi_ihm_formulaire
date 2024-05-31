from flask import Flask,render_template,request
from capitales import capitales
from fonctions import *

app = Flask(__name__)

@app.route('/')
def accueil():
  return render_template("index.html")

@app.route('/jouer', methods=['POST'])
def jouer():
    # récupération de la méthode d'envoi
    rep = request.form
    reponse = rep.to_dict()
    print(reponse)
    pays = reponse['pays']
    score = eval(reponse['score'])
    if 'capitale' in reponse.keys():
        capitale = reponse['capitale']
    else:
        capitale = ''
    
    # Construction du dictionnaire qui contient le pays et les trois capitales
    if capitale == '':
       context = questionnaire(capitales)
       context['score'] = score - 1
       return render_template("jouer.html", **context)
    elif verifier(capitales,pays,capitale):
        context = questionnaire(capitales)
        context['score'] = score + 1
        return render_template("jouer.html", **context)
    else:
        return render_template("perdu.html", pays=pays, score=score, capitale = capitales[pays])

app.run(debug=True)
