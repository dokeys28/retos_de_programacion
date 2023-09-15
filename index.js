const LISTADEPALABRAS = ['penecito', 'agapito'];
const OCU = ['p_ne_ito', 'a_a_it_'];
const INICIAR = document.querySelector('.iniciar');
const BOTON = document.querySelector('.enviar');
const PALABRA = document.querySelector('.palabra');
const USUARIO = document.querySelector('.input');
const TEXTO_API = document.querySelector('.api');
const BOTON_API = document.querySelector('.apib');

let palabra_oculta;
let palabra_random;
BOTON.disabled = true;

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


function consumir_api(){
// URL de la API que quieres consumir
const url = 'https://mi_api-1-g7151897.deta.app/usuarios';

// Realizar una solicitud GET a la API
fetch(url)
  .then(response => {
    // Verificar si la solicitud fue exitosa (código de estado 200)
    if (!response.ok) {
      throw new Error('Error al consumir la API. Código de estado: ' + response.status);
    }
    // Convertir la respuesta a formato JSON (si la API devuelve JSON)
    return response.json();
  })
  .then(data => {
    // Ahora puedes trabajar con los datos como lo necesites
    TEXTO_API.innerHTML = JSON.stringify(data)
  })
  .catch(error => {
    // Si hay un error, manejarlo adecuadamente
    console.error('Error:', error);
  });


}
function ingresar_usuario(){
// URL de la API que quieres consumir
const url = 'https://mi_api-1-g7151897.deta.app/usuario';
let bodyContent = JSON.stringify({"nombre":"Pedro",
  "edad": 18
});

// Realizar una solicitud GET a la API
fetch(url, {method: ['POST'], body: bodyContent})
  .then(response => {
    // Verificar si la solicitud fue exitosa (código de estado 200)
    if (!response.ok) {
      throw new Error('Error al consumir la API. Código de estado: ' + response.status);
    }
    // Convertir la respuesta a formato JSON (si la API devuelve JSON)
    return response.json();
  })
  .then(data => {
    // Ahora puedes trabajar con los datos como lo necesites
    TEXTO_API.innerHTML = data
  })
  .catch(error => {
    // Si hay un error, manejarlo adecuadamente
    console.error('Error:', error);
  });


}


INICIAR.addEventListener('click',()=>{
    inicio();

});
BOTON.addEventListener('click',()=>{

    verificar();
});


BOTON_API.addEventListener('click',consumir_api);
