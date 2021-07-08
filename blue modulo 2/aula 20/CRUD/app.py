from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# banco de dados

user = 'zpjdfprw'
password = 'LQYyr4HAMd_sKdJ6LN5oe6w8qAow5D5o'
host = 'tuffi.db.elephantsql.com'
database = 'zpjdfprw'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'password'

db = SQLAlchemy(app)
# filmes db

class Filmes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)

    def __init__(self, nome, imagem_url):
        self.nome = nome
        self.imagem_url = imagem_url
    
    @staticmethod
    def read_all():
        # select * from filmes order by id desc
        # return Filmes.query.order_by(Filmes.id.desc()).all()
        return Filmes.query.order_by(Filmes.id.asc()).all()

    @staticmethod
    def read_single(registro_id):
        # select * from filmes where id =1
        return Filmes.query.get(registro_id)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update (self, new_data):
        self.nome = new_data.nome
        self.imagem_url = new_data.imagem_url
        self.save()

        



# rotas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read')
def read_all():
    registros = Filmes.read_all()
    return render_template('read_all.html', registros = registros)

@app.route('/read/<registro_id>')
def read_single(registro_id):
    registro  = Filmes.read_single(registro_id)
    print (registro)
    return render_template('read_single.html', registro = registro)

@app.route('/create', methods=('GET', 'POST'))
def create():
    id_atribuido = None

    if request.method == 'POST':
        form = request.form

        registro = Filmes(form['nome'], form['imagem_url'])
        registro.save()
        id_atribuido = registro.id
    return render_template('create.html', id_atribuido = id_atribuido)


@app.route('/update/<registro_id>', methods= ('GET', 'POST'))
def update(registro_id):
    sucesso = None
    registro = Filmes.read_single(registro_id)

    if request.method == 'POST':
        form = request.form
        new_data = Filmes(form['nome'], form['imagem_url'])
        registro.update(new_data)
        sucesso = True
    return render_template('update.html', registro = registro, sucesso = sucesso )


if __name__ == "__main__":
    app.run(debug=True)