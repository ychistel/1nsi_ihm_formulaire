from flask import Flask,render_template,request

def parametrer(rep):
  reponse = dict()



app = Flask(__name__)

@app.route('/')
def accueil():
  return render_template("index.html")

@app.route('/formulaire')
def formulaire():
  return render_template("formulaire.html")

@app.route('/login')
def login():
  return render_template("login.html")

@app.route('/404')
def erreur():
  return render_template("404.html")

@app.route('/reponse', methods=['GET','POST'])
def reponse():
  # récupération de la méthode d'envoi
  if request.method == 'GET':
    rep = request.args
  else:
    rep = request.form
  try:
    valeurs=rep.to_dict()
    return render_template("reponse.html", valeur=valeurs)
  except:
    return erreur()

@app.route('/auth',methods = ['POST'])
def auth():
  rep = request.form
  n = rep['nom']
  pwd = rep['passwd']
  if n == 'bob' and pwd == 'Eponge!':
    return render_template("auth.html",nom = n, passwd = pwd)
  else:
    return render_template("login.html")


app.run(debug=True)
