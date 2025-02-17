"""Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no."""
#Funcion para verificar si un año es bisiesto 
def es_bisiesto(ano):
    #Un año es bisiesto si divisible por 4
    #No es bisiesto si es divisible por 100, excepto si también es divisible por 400
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): 
        return True
    else:
        return False
    
#Solicita al usario que ingrese un año
ano = int(input("Por favor, ingrese un año: "))

#Verificar si el año ingresado es bisiesto
if es_bisiesto(ano):
    print(f"El año {ano} es bisiesto.")

else:
    print(f"El año {ano} no es bisiesto")