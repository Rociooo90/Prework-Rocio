"""Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.)"""

def determinar_dia_semana(numero):
    dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']

    #verificar si el número esta dentro del rango válido
    if numero >= 1 and numero <= 7:
            #Obtener el nombre del día correspondiente al número ingresado
            dia = dias_semana[numero - 1]
            return dia
    else:
          return "Número fuera de rango. Introduce un número entre 1 y 7."
    
def main():
      #Solicitar al usuario que introduzca un número del 1 al 7
      numero = int(input("Ingresa un número del 1 al 7 para determinar el día de la semana: "))
      
      #Llamar a la función determinar_dia_semana para obtener el nombre del día
      nombre_del_dia = determinar_dia_semana(numero)

      #Mostrar el resultado
      print(f"El día correspondiente al número {numero} es {nombre_del_dia}")

     
