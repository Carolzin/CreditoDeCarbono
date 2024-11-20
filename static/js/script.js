// A função escolhaCampo permite que apenas um dos campos sejam preenchidos
function escolhaCampo(outroCampoId, campoAtual) {
    const outroCampo = document.getElementById(outroCampoId);

    if (campoAtual.value.trim() !== "") {
        outroCampo.value = "";
        outroCampo.removeAttribute('required'); 
        campoAtual.setAttribute('required', 'required'); 
    } else {
        outroCampo.setAttribute('required', 'required');
    }
}

// Verifica requisição para que ao menos um dos campos sejam preenchidos
document.querySelector('form').addEventListener('submit', function(event) {

    // Eletricidade
    const consumoKwh = document.getElementById('consumo_kwh');
    const valorReais = document.getElementById('valor_reais');

    if (consumoKwh.value.trim() === "" && valorReais.value.trim() === "") {
        consumoKwh.setAttribute('required', 'required');
        valorReais.setAttribute('required', 'required');
    }

    // Gás
    const consumoBotijao = document.getElementById('consumo_botijao');
    const consumoGasEncanado = document.getElementById('consumo_gas_encanado');

    if (consumoBotijao.value.trim() === "" && consumoGasEncanado.value.trim() === "") {
        consumoBotijao.setAttribute('required', 'required');
        consumoGasEncanado.setAttribute('required', 'required');
    }

    // Transportes
    const consumoCombustivel = document.getElementById('consumo_combustivel');
    const valorCombustivel = document.getElementById('valor_combustivel');

    if (consumoCombustivel.value.trim() === "" && valorCombustivel.value.trim() === "") {
        consumoCombustivel.setAttribute('required', 'required');
        valorCombustivel.setAttribute('required', 'required');
    }
});

// Reseta o forms quando a página for recarregada
window.onload = function() {
    document.querySelector('form').reset(); 
}

// Função para retornar ao topo da página
function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

window.onscroll = function() {
    const button = document.getElementById('voltarTop');
    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        button.style.display = 'block';
    } else {
        button.style.display = 'none';
    }
};