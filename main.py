from flask import Flask


#inicializacao
app = Flask(__name__)

configure_all(app)

#execucoes
app.run(debug=True)