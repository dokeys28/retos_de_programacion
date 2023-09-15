const INPUT = document.querySelector('.input')
const BOTON = document.querySelector('.boton')
const GATO = document.querySelector('.gato')


BOTON.addEventListener('click',()=>{
    GATO.src = 'loading.gif'
    if (INPUT.value !== ""){
        // Hacer una solicitud GET a la API
        fetch(`https://cataas.com/cat/says/${INPUT.value}`)
        .then(response => {
            // Verificar si la solicitud fue exitosa (código de estado 200)
            if (!response.ok) {
            throw new Error('Error al obtener la imagen. Código de estado: ' + response.status);
            }
            return response.blob(); // Convertir la respuesta a un objeto Blob
        })
        .then(blob => {
            // Crear una URL para la imagen
            const imgUrl = URL.createObjectURL(blob);

            // Crear un elemento de imagen y establecer su fuent
            GATO.src = imgUrl;
        })
        .catch(error => {
            // Si hay un error, manejarlo adecuadamente
            console.error('Error:', error);
        });

        INPUT.value = ""
    }
})