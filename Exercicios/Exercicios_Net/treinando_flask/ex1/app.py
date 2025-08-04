from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index"


def teste():
    return "<p>testando 1</p>"


def teste2():
    return "<p>testando 2</p>"

#3 parametros principais REGRA="/teste", ENDPOINT="teste", viewfunction=def teste
app.add_url_rule("/teste", "teste", teste)
app.add_url_rule("/teste2", "teste2", teste2)

app.run(debug=True, port="5000")