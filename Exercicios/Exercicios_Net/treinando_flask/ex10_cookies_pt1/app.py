from flask import Flask, render_template, request, make_response

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/setcookie', methods=['GET', 'POST'])
def setcookie():
    resp = make_response(render_template('setcookie.html'))

    if request.method == 'POST':
        dados = request.form['c']#da acesso aos parametros de POST
        resp.set_cookie('testeCookie', dados)

    return resp


@app.route('/getcookie')
def getcookie():
    cookiename = request.cookies.get('testeCookie')
    return '<h1>Valor cookie é: {}</h1>'.format(cookiename)


if __name__ == '__main__':
    app.run(debug=True)
