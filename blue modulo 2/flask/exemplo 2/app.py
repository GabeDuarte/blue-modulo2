from flask import Flask
app = Flask (__name__)

@app.route("/")
def home():
    return "Hello, Gabriel !"

@app.route("/rota2")
def rota2():
    return "<h1> Essa é a pagina da segunda rota</h1> "

@app.route("/blue")
def blue():
    return "<h1> eu sou blue </h1>"

@app.route("/blue/bluemer")
def bluebluemer():
    return "<h3> eu sou o cara! </h3"


if __name__ == "__main__":
    app.run(debug=True)