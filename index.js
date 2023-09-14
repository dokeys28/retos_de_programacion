const LISTADEPALABRAS = ['penecito', 'agapito'];
const OCU = ['p_ne_ito', 'a_a_it_'];
const INICIAR = document.querySelector('.iniciar');
const BOTON = document.querySelector('.enviar');
const PALABRA = document.querySelector('.palabra');
const USUARIO = document.querySelector('.input');
const PALABRA_API = document.querySelector('.api');
const BOTON_API = document.querySelector('.apib');

let palabra_oculta;
let palabra_random;
BOTON.disabled = true;
const api_key = 'b0bC9dab48z4_ghLJNoARpQwqZacdrkWYpco9RDiZ3g8g';

function inicio(){
    let numero_random = Math.round(Math.random());
    palabra_random = LISTADEPALABRAS[numero_random];
    palabra_oculta = OCU[numero_random];
    PALABRA.innerHTML = palabra_oculta;
    INICIAR.disabled = true;
    USUARIO.value = "";
    BOTON.disabled = false;
};

function verificar(){
    if (USUARIO.value == palabra_random){
        PALABRA.innerHTML = palabra_random;
        INICIAR.disabled = false;
        BOTON.disabled = true;
        
    }else{
        PALABRA.innerHTML = 'klk mamaguevo';
        INICIAR.disabled = false;
        BOTON.disabled = true;
    };
};

async function buscar_api(){
  await fetch('https://miapi-1-a9187628.deta.app/usuarios/',{headers:{'Authorization': `APIKEY ${api_key}`},method: 'GET'})
  .then(response => response.json())
  .then(data=>{
    PALABRA_API.innerHTML = data
  });
}


INICIAR.addEventListener('click',()=>{
    inicio();

});
BOTON.addEventListener('click',()=>{

    verificar();
});

BOTON_API.addEventListener('click',()=>{
    buscar_api()
    console.log('klk')
})