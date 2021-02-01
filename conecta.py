from flask import Flask
from machine_learning import precisao

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

#metodo da api para verificar a precisão da inteligencia artificial
@app.route("/precision", methods=["GET"])
def precision():
    return ("teste")
app.run()