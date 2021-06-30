from flask import Flask, render_template

app = Flask(__name__)

# create
# read - leitura (select)
# update
# delete

# read () - trabalhar com os dados mockados

registros = [
    {
        'id':1,
        'nome': 'À Espera de um Milagre',
        'imagem_url': 'https://i.pinimg.com/originals/96/83/86/9683865e5dc659f1823840d312bee2a5.jpg'
    },

    {
        'id':2,
        'nome': 'O Paizão',
        'imagem_url': 'http://4.bp.blogspot.com/_9Av0As0ieq4/SXDPQH4pFYI/AAAAAAAAAus/wj6Dw0-hJQM/s400/opaizao.jpg'
    },

    {
        'id':3,
        'nome': 'Alô Amigos',
        'imagem_url': 'https://br.web.img2.acsta.net/pictures/14/03/06/15/39/175511.jpg'
    },

    {
        'id':4,
        'nome': 'As Crônicas de Spiderwick',
        'imagem_url': 'https://www.themoviedb.org/t/p/w500/7YABWxerZXH705J34qaUbvJLXVz.jpg'
    },

    {
        'id':5,
        'nome': 'Histórias Cruzadas',
        'imagem_url': 'https://mulheres.apmppr.com.br/storage/women-movies/2018.12.20-11.23.43.jpg'
    },
    {
        'id':6,
        'nome': 'Cidade de Deus',
        'imagem_url': 'https://cdn.tlc-massive.com/shain/v1/dataservice/ResizeImage/$value?Format=%27jpg%27&Quality=85&ImageId=%27211515.jpg%27&ImageUrl=%27211515.jpg%27&EntityType=%27Item%27&EntityId=%277389%27&device=web_browser&subscriptions=Anonymous&Width=360&Height=540'
    }
]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/read')
def read_all():
    return render_template('read_all.html', registros = registros)



@app.route('/read/<id_registro>')
def read_single(id_registro):
    return 'Em Construção: Visualizar registro de ID '+ id_registro



if __name__ == "__main__":
    app.run(debug=True)