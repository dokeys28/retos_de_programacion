import datetime
# /*
#  * Crea una función que sea capaz de detectar si existe un viernes 13 
# en el mes y el año indicados.
def viernes_13(month, year )-> bool:
    if datetime.date(year,month,13).weekday() == 4:
        return True
    else:
        return False

    
#  * - La función recibirá el mes y el año y retornará verdadero o falso.
#  */

print(viernes_13(7,1973))