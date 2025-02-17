"""
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
"""
def es_palindromo(palabra):
    #Convertimos la palabra a minñusculas y eliminamos los espacios en blanco
    palabra = palabra.lower().replace(" ", "")
    #Comparamos la palabra con su reverso
    return palabra == palabra[::-1]

#Solicitamos al usuario que ingrese una palabra
palabra_usuario = input("Ingresa una palabra: ")

#Verificamos si la palabra es un palíndromo
if es_palindromo(palabra_usuario):
        print(f'"´{palabra_usario}" es un palíndromo.')
else:
      print(f'"´{palabra_usario}" no es un palíndromo.')