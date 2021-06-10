from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    nome = "Badass Sonic"
    hp = 2000

    exibir_imagem = True
    imagem = "https://i.pinimg.com/originals/84/90/f0/8490f0cab98f44a6e905a72cb61b72aa.gif"

    return render_template(
        "index.html",
        nome = nome,
        hp = hp,
        exibir_imagem = exibir_imagem,
        imagem = imagem
    )


if __name__ == "__main__":
    app.run(debug=True)