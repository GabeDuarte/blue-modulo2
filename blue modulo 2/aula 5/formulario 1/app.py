from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def home():

    if request.method == "POST":
        usuario_nome = request.form["usuario_nome"]
        usuario_sobrenome = request.form["usuario_sobrenome"]
        apenas_uma_opcao = request.form["apenas_uma_opcao"]
        multiplas_opcoes = request.form["multiplas_opcoes"]
        
        print()
        print(f'Nome do usuario: {usuario_nome}')
        print()
        print(f'Sobrenome do usuario: {usuario_sobrenome}')
        print()
        print(f'Apenas uma opção: {apenas_uma_opcao}')
        print()
        print(f'Multiplas opções: {multiplas_opcoes}')
        print()
        
    return render_template('index.html')        




if __name__ == "__main__":
    app.run(debug=True)