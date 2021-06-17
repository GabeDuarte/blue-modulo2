const botao = document.querySelector('#botao')

function botaoFoiClicaddo(){
    alert ('Você clicou no botão');
    alert ("Quem mandou clicar no botão? ");
}


botao.addEventListener("click", botaoFoiClicaddo);
botao.innerHTML ="Clique aqui!"