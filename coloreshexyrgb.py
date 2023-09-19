# /*
#  * Crea las funciones capaces de transformar colores HEX
#  * a RGB y viceversa.
#  * Ejemplos:
#  * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
#  * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
#  */

#0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#A, B, C, D, E, F --- 10, 11, 12, 13, 14, 15
#multiplicar el primer valor * 16, y
# al resultado de esa multiplicación sumarle el segundo valor.

diccionarioHEX = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    }

def pares(parHEX):
    primer_numero = diccionarioHEX[parHEX[0]] * 16
    par =  primer_numero + diccionarioHEX[parHEX[1]]
    return par

def HEX_to_RGB(color_HEX: str) -> tuple:
    if len(color_HEX) == 7:
        color_HEX = color_HEX.removeprefix('#')
        rgblistado = []
        #separar en pares
        for n in range(0,6,2):
            par_rgb = pares(color_HEX[n:n+2])
            rgblistado.append(par_rgb)
        
        rgb = tuple(rgblistado)
        return rgb
    else:
        return 'Formato incorrecto'

print(HEX_to_RGB('#000000'))