

const pessoa = {
    nome: 'Tony',
    sobrenome: 'Stark',
    idade: 52,

    feliz: true,

    imagemRaiva: 'https://i.pinimg.com/originals/c2/4d/ab/c24dab77eba256cd0aca815371b52252.jpg',
    imagemFeliz: 'https://pbs.twimg.com/media/D5R927nUIAAfyH1.jpg',
}

const elementoNome = document.getElementById('nome');
const elementoSobrenome = document.getElementById('sobrenome');
const elementoIdade = document.getElementById('idade');

elementoNome.innerText = pessoa.nome;
elementoSobrenome.innerText = pessoa.sobrenome;
elementoIdade.innerText = pessoa.idade;


function atualizarHumor(){
    const elementoImagem = document.getElementById('img');
    const bloco_humor = document.getElementById('bloco_humor')

    if (pessoa.feliz){
        elementoImagem.src = pessoa.imagemFeliz;
        bloco_humor.innerText = pessoa.nome + "tá feliz! "  ;
    }
    else{
        elementoImagem.src = pessoa.imagemRaiva;
        bloco_humor.innerText = pessoa.nome + 'tá com raiva!';
    }
}

atualizarHumor();

const botaoAlterarHumor = document.getElementById('alterarHumor');
botaoAlterarHumor.addEventListener('click', function(){
    pessoa.feliz = !pessoa.feliz;

    atualizarHumor()

});