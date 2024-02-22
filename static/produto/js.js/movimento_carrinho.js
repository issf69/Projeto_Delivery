// movimento_carrinho.js

// Obtém a referência para o elemento do carrinho
var carrinho = document.getElementById('carrinho');

// Define a posição inicial do carrinho
var posicao = 0;

// Função para mover o carrinho
function moverCarrinho() {
    // Atualiza a posição do carrinho
    posicao += 1;
    // Define a posição do carrinho no estilo CSS
    carrinho.style.left = posicao + 'px';
    // Define o intervalo de tempo para o próximo movimento
    setTimeout(moverCarrinho, 10); // Altere este valor para ajustar a velocidade do movimento
}

// Chama a função para iniciar o movimento do carrinho
moverCarrinho();
