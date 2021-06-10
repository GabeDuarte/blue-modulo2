from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    nome = "Betão"
    idade = "42"
    feliz = False
    imagem1 = "https://www.gifmania.co.uk/Space-Animated-Gifs/Animated-Astronomy/Astronomers/Albert-Einstein/Albert-Einstein-laughing-49614.gif"
    imagem2 = "http://2.bp.blogspot.com/-rvDzKZVwNow/TrUieZVixGI/AAAAAAAAA00/EAbV6f2q_1A/s1600/einstein.gif"
    texto1 = "Betão tá feliz!!"
    texto2 = "Betão tá doido!"

    return render_template(
        "index.html",
        nome = nome,
        idade = idade,
        feliz = feliz,
        imagem1 = imagem1,
        imagem2 = imagem2,
        texto1 = texto1,
        texto2 = texto2
)


if __name__ == "__main__":
    app.run(debug=True)