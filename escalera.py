# /*
#  * Crea una función que dibuje una escalera según su número de escalones.
def dibujar_escalera(numero_de_escalones: int):
#  * - Si el número es positivo, será ascendente de izquiera a derecha.
    escalon_superior: str = '_'
    escalon_ascendente : str = '_|'
    escalon_descendente: str = '|_'
    numero_de_espacios_escalon_superior: int = abs(numero_de_escalones) * len(escalon_ascendente)
    
    if numero_de_escalones > 0:
        print(' ' * numero_de_espacios_escalon_superior + escalon_superior)
        for _ in range(numero_de_escalones):
            if numero_de_espacios_escalon_superior > 0:
                numero_de_espacios_escalon_superior -= len(escalon_ascendente)
            print(' ' * numero_de_espacios_escalon_superior + escalon_ascendente)
#  * - Si el número es negativo, será descendente de izquiera a derecha.
    if numero_de_escalones < 0:
        numero_de_espacios_escalon_superior: int = abs(numero_de_escalones) * len(escalon_ascendente)
        numero_escalones_negativos = 0
        print(escalon_superior)
        escalon_superior_colocado = False
        for _ in range(abs(numero_de_escalones)):
            if not escalon_superior_colocado:
                numero_escalones_negativos += len(escalon_superior)
                escalon_superior_colocado = True
                print(' ' * numero_escalones_negativos + escalon_descendente)
            
            if numero_escalones_negativos < numero_de_espacios_escalon_superior:
                numero_escalones_negativos += len(escalon_descendente)
            print(' ' * numero_escalones_negativos + escalon_descendente)

#  * - Si el número es cero, se dibujarán dos guiones bajos (__).
    if numero_de_escalones == 0:
        print(escalon_superior * 2)
#  * 
#  * Ejemplo: 4
#  *         _
#  *       _|       
#  *     _|
#  *   _|
#  * _|
#  * 
#  */

dibujar_escalera(4)
dibujar_escalera(-4)
dibujar_escalera(0)