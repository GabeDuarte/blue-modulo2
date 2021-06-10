from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    nome_jogador = "Gabriel"
    valor_premio = "100.000"
    premio = True
    return render_template(
        "index.html", 
        nome_jogador = nome_jogador,
        premio = premio,
        valor_premio = valor_premio,
)    




if __name__ == "__main__":
    app.run(debug=True)
