#Reservas de un restaurante
# Ver disponibilidad:
from datetime import date
import random



class Reserva:
    def __init__(self, dia, reservada):
        self.reservada= reservada
        self.fecha: date = date(2023,9,dia)


class Manager:
    def __init__(self) -> None:
        self.reservas = []
        self.fechas = []
        self.fechas_disponibles = []
        
        #guardando objetos fecha
        for n in range(30):
            self.fechas.append(Reserva(n+1, False))
    
    def ver_disponibilidad(self):
        self.fechas_disponibles = []
        for f in self.fechas:
            if not f.reservada:
                self.fechas_disponibles.append(f.fecha.day)
        
        if len(self.fechas_disponibles)> 0:
            return self.fechas_disponibles
        else:
            return 'No hay fechas disponibles'
                        
    # Hacer una reserva:
    def reservar(self, dia: int):
        for f in self.fechas:
            if f.fecha.day == dia and not f.reservada:
                f.reservada = True
    
    # Ver reservas: 
    def ver_reserva(self):
        self.reservas = []
        for f in self.fechas:
            if f.reservada:
                self.reservas.append(f.fecha.day)
        return self.reservas
            
    # Cancelar una reserva: 
    def cancelar_reserva(self, dia : int):
        for f in self.fechas:
            if f.fecha.day == dia and f.reservada:
                f.reservada = False
                self.reservas.remove(dia)
    

jose = Manager()

for _ in range(16):
    jose.reservar(random.randint(1,30))
    
print(f'Disponibilidad: {jose.ver_disponibilidad()}')
print(f'Reservas: {jose.ver_reserva()}')
jose.cancelar_reserva(random.randint(1,30))
print(f'Reservas: {jose.ver_reserva()}')
print(f'Disponibilidad: {jose.ver_disponibilidad()}')
