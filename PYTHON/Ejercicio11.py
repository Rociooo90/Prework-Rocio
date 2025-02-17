"""Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual."""
import datetime

def calcular_edad_actual(anio_nacimiento):
    #Obtener el año actual
    anio_actual = datetime.datetime.now().year

    #Calcular la edad restando el año de nacimiento al año actual
    edad = anio_actual - anio_nacimiento

    return edad 

def main():
     #Solicitar al usuario que ingrese su año de nacimiento
     anio_nacimiento = int(input("Ingrese su año de nacimiento (YYYY): "))

     #Calcular la edad usando la función calcular_edad
     edad = calcular_edad_actual(anio_nacimiento)

     #Mostrar la edad calculada 
     print(f"Tienes aproximadamente {edad} años.")
   

