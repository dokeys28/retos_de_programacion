# /*
#  * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#  * - El juego comienza proponiendo una palabra aleatoria incompleta
#  *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
import random

LISTA_DE_PALABRAS = ['acidosis metabolica','papotico','lapiz lazuli','crucigrama','pentavalente']

def saltos(palabra):
    print(f'\n{palabra}\n')

    
class Palabra:
    def __init__(self):
        self.palabra_random = self.elegir_palabra()
        self.palabra_oculta = self.ocultar_palabra()
        
    def elegir_palabra(self):
        palabra_random = random.choice(LISTA_DE_PALABRAS)
        return palabra_random
            
    def porcentar_palabra(self):
        porciento_palabra_random = len(self.palabra_random) * 0.60
        return int(porciento_palabra_random)

    def obtener_numero_random(self):
        numero_random = random.randint(0, (len(self.palabra_random)-1))
        return numero_random
    
    def ocultar_palabra(self):
        self.palabra_oculta = list(self.palabra_random)
        for _ in range(self.porcentar_palabra()):
            numero_random = self.obtener_numero_random()
            if self.palabra_oculta[numero_random] != '_' and self.palabra_oculta[numero_random]!= ' ':
                self.palabra_oculta[numero_random] = '_'
        return "".join(self.palabra_oculta)
    
    def actualizar_palabra(self, respuesta):
        #si es palabra completa
        if respuesta == self.palabra_random:
            print('Si')
            self.palabra_oculta = respuesta
        #si es letra
        else:
            self.palabra_oculta = list(self.palabra_oculta)
            for i,l in enumerate(self.palabra_random):
                if respuesta == l:
                    self.palabra_oculta[i] = respuesta
            self.palabra_oculta = "".join(self.palabra_oculta)
   
    def mostrar_palabra(self):
        return self.palabra_oculta
    
        
class Verificador:
    def __init__(self, juego):
        self.palabra = juego.palabra
        
    def verificar(self, palabra_adivinada):
        if palabra_adivinada in self.palabra.palabra_random:
            self.palabra.actualizar_palabra(palabra_adivinada)
        return self.palabra.mostrar_palabra()

class Juego:
    def __init__(self) -> None:
        self.numero_de_intentos = 0
        self.limite_de_intentos = 4
        self.palabra = Palabra()
        self.verificador = Verificador(self)
       
    
    def correr(self):
        saltos(self.palabra.palabra_oculta)
        while self.numero_de_intentos <= self.limite_de_intentos:
            respuesta_usuario = input(f'Adivina la palabra: ')
            self.numero_de_intentos += 1
            palabra_completa = self.verificador.verificar(respuesta_usuario)
            saltos(palabra_completa)
            if '_' not in palabra_completa:
                saltos('GANASTE')
                break
        else:
            saltos('PERDISTE')
        saltos('GAME OVER')

#  * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#  *   la palabra a adivinar)
#  *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#  *     uno al número de intentos
#  *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  *     al número de intentos
#  *   - Si el contador de intentos llega a 0, el jugador pierde
#  * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
#  * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
#  */

Juego().correr()