from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/admin/")
def admin():
    return "<h1>Olá Admin</h1>"


@app.route("/guest/<guest>/")
def guest(guest):
    return "<p> olá guest <b>%s</b></p>" % guest


@app.route("/pesquisa/pudim")
def pesquisa():
    return redirect('http://pudim.com')


#redireciona as rotas, digita no navegador e ele muda a rota! http://localhost:5000/user/admin ele vai para http://localhost:5000/admin/
@app.route("/user/<name>/")
def user(name):
    if name == "admin":
        return redirect(url_for('admin'))#def 'admin'
    else:
        return redirect(url_for('guest', guest=name))

app.run(debug=True, port="5000")
