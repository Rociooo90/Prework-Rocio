"""Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario"""

def contar_palabras(oracion):
    #Dividir la oración en palabras utilizando espacios como delimitadores
    palabras = oracion.split()
    
    #Contar la cantidad de palabras 
    cantidad_palabras = len(palabras)
    return cantidad_palabras 

#Solicitar al usuario que ingrese una oración
oracion = input ("Por favor ingrese una oracion: ")

#cONTAR LAS palabras en la oración ingresada
cantidad = contar_palabras(oracion)

#Mostrar el resultado
print(f"La cantidad de palabras en la oración ingresada es: {cantidad}")