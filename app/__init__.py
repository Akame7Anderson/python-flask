from flask import Flask, render_template 
app = Flask(__name__) #instanciando classe flask

#endereço do site
@app.route('/') #rota principal
@app.route('/index') #rota alternativa
def index():
  #return "Olá cidadão(ã)"
  return render_template('index.html')