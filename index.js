const LISTADEPALABRAS = ['penecito', 'agapito'];
const OCU = ['p_ne_ito', 'a_a_it_'];
const INICIAR = document.querySelector('.iniciar');
const BOTON = document.querySelector('.enviar');
const PALABRA = document.querySelector('.palabra');
const USUARIO = document.querySelector('.input');

let palabra_oculta;
let palabra_random;

function inicio(){
    let numero_random = Math.round(Math.random());
    palabra_random = LISTADEPALABRAS[numero_random];
    palabra_oculta = OCU[numero_random];
    PALABRA.innerHTML = palabra_oculta;
    INICIAR.disabled = true;
    USUARIO.value = "";
};

function verificar(){
    if (USUARIO.value == palabra_random){
        PALABRA.innerHTML = palabra_random;
        INICIAR.disabled = false
    }else{
        PALABRA.innerHTML = 'klk mamaguevo';
        INICIAR.disabled = false
    };
};


INICIAR.addEventListener('click',()=>{
    inicio();

});
BOTON.addEventListener('click',()=>{

    verificar();
});
