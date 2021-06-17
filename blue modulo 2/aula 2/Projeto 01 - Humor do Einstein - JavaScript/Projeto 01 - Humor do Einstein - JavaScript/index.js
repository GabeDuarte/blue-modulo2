// Definir dados iniciais

const pessoa = {
    nome: 'Betão',
    sobrenome: 'Einstein',
    idade: 42,

    doido: true,

    imagemSerio: 'https://upload.wikimedia.org/wikipedia/commons/5/50/Albert_Einstein_%28Nobel%29.png',
    imagemDoido: 'https://www.hypeness.com.br/1/2017/08/EinsteinL3.jpg',
}

// Atualizar dados

const elementoNome = document.getElementById('nome');
const elementoSobrenome = document.getElementById('sobrenome');
const elementoIdade = document.getElementById('idade');

elementoNome.innerText = pessoa.nome;
elementoSobrenome.innerText = pessoa.sobrenome;
elementoIdade.innerText = pessoa.idade;

// Atualizar humor
function atualizarHumor() {
    const elementoImagem = document.getElementById('imagem');
    const blocoHumor = document.getElementById('bloco_humor');

    if (pessoa.doido) {
        elementoImagem.src = pessoa.imagemDoido;
        blocoHumor.innerText = pessoa.nome + ' tá doido!';
    } else {
        elementoImagem.src = pessoa.imagemSerio;
        blocoHumor.innerText = pessoa.nome + ' tá sério!';
    }
}

atualizarHumor();

// Alterar humor

const botaoAlterarHumor = document.getElementById('alterarHumor');
botaoAlterarHumor.addEventListener('click', function () {
    pessoa.doido = !pessoa.doido;

    atualizarHumor();
});
