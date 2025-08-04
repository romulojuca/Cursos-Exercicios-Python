from flask import Flask

app = Flask(__name__)


@app.route("/hello/")
@app.route("/hello/<name>/")
def hello(name=" "):
    return "<h1>Hello {}</h1>".format(name)


@app.route("/blog/")
@app.route("/blog/<int:id>/")
def blog(id=-1):
    if id >= 0:
        return "Blog Info {}".format(id)
    else:
        return "Blog Todo"


@app.route("/blog2/")
@app.route("/blog2/<float:id>/")
def blog2(id=0):
    if id >= 0:
        return "Blog Info {}".format(id)
    else:
        return "Blog Todo"


app.run(debug=True, port="5000")
