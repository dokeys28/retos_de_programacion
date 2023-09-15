import requests

# URL de la API que quieres consumir
url = 'https://miapi-1-a9187628.deta.app/usuario/Luis'

# Realizar una solicitud GET a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Convertir la respuesta a formato JSON (si la API devuelve JSON)
    datos = response.json()
    print(datos)
    # Ahora puedes trabajar con los datos como lo necesites
else:
    # Si la solicitud no fue exitosa, maneja el error adecuadamente
    print('Error al consumir la API. Código de estado:', response.status_code)
