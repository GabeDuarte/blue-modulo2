from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nome = "betão"
    idade = "42"
    humor = True
    img = "https://www.gifmania.co.uk/Space-Animated-Gifs/Animated-Astronomy/Astronomers/Albert-Einstein/Albert-Einstein-laughing-49614.gif"
    texto ="Betão tá feliz!"

    return render_template(
        "index.html",
        nome = nome,
        idade= idade,
        humor = humor,
        img = img,
        texto = texto
)

@app.route("/doido")
def triste():
    nome = "betão"
    idade = "42"
    humor = True
    img = "https://2.bp.blogspot.com/-rvDzKZVwNow/TrUieZVixGI/AAAAAAAAA00/EAbV6f2q_1A/s1600/einstein.gif"
    texto ="Betão tá doido!"

    return render_template(
        "index.html",
        nome = nome,
        idade= idade,
        humor = humor,
        img = img,
        texto = texto
)


if __name__ == "__main__":
    app.run(debug=True)