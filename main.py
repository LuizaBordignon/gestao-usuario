from flask import Flask
from configuration import configure_all

#inicializacao
app = Flask(__name__)

configure_all(app)

#execucoes
app.run(debug=True)