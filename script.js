// Formulário Multi-Etapas
const formPaginas = document.querySelectorAll(".form-pagina");
const proxBtn = document.querySelector("#proxBtn");
const voltBtn = document.querySelector("#voltBtn");
const progressPaginas = document.querySelectorAll(".pagina");

let formPaginaIndex = 0;

progressPaginas[0].classList.add("active");

// Função para avançar de página
proxBtn.addEventListener("click", () => {
    if (formPaginaIndex < formPaginas.length - 1) {
        formPaginaIndex++;
        updateFormPaginas();
        updateProgressBar();
    }
});

// Função para voltar à página anterior
voltBtn.addEventListener("click", () => {
    if (formPaginaIndex > 0) {
        formPaginaIndex--;
        updateFormPaginas();
        updateProgressBar();
    }
});

// Atualiza as páginas do formulário
function updateFormPaginas() {
    formPaginas.forEach((pagina, idx) => {
        if (idx === formPaginaIndex) {
            pagina.classList.add("active");
            pagina.style.display = "flex"; 
        } else {
            pagina.classList.remove("active");
            pagina.style.display = "none";  
        }
    });

    // Desabilita a vizualição do botão de "Voltar" na primeira página de exibição
    if (formPaginaIndex === 0) { 
        voltBtn.style.display = "none"; 
    } else {
        voltBtn.style.display = "inline-block";  
    }
}

// Atualiza a barra de progresso
function updateProgressBar() {
    progressPaginas.forEach((pagina, idx) => {
        if (idx <= formPaginaIndex) {
            pagina.classList.add("active");
        } else {
            pagina.classList.remove("active");
        }
    });
}

// Atualiza o texto do botão "proxBtn"
document.addEventListener('DOMContentLoaded', function() {
    const proxBtn = document.getElementById('proxBtn');

    function atualizarTextoBotao() {
        const paginas = document.querySelectorAll('.form-pagina');
        paginas.forEach((pagina, index) => {
            if (pagina.classList.contains('active')) {
                if (index === 3) {  // Página 4 
                    proxBtn.innerText = 'Resultado';
                } else if (index === 4) {  // Página 5
                    proxBtn.innerText = 'Finalizar';
                } else if (index === 5) {  // Página 6
                    proxBtn.innerText = 'Compensar (R$00,00)';
                } else {
                    proxBtn.innerText = 'Próximo';
                }
            }
        });
    }

    document.getElementById('proxBtn').addEventListener('click', atualizarTextoBotao);
    document.getElementById('voltBtn').addEventListener('click', atualizarTextoBotao);
    
    atualizarTextoBotao();
});


updateFormPaginas();

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

