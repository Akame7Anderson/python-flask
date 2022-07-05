from flask import Flask, render_template
app = Flask(__name__) #Instanciando classe Flask.

#Endereço do site.
@app.route('/') #Rota principal.
@app.route('/index') #Rota alternativa.
def index():
    #return "Hello, world!"
    nome='Anderson' #Variável.
    dados={"idade":"20 anos", "cidade":"Santa Rosa"} #Variável.
    return render_template('index.html',nome=nome, dados=dados)
@app.route('/contato')
def contato():
    return render_template('contato.html')
@app.route('/produtos')
def produtos():
    return render_template('produtos.html')      







app.run()