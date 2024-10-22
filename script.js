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

updateFormPaginas();
