"""Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario."""

def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        return pares, impares 

def main():
    try:
        entrada = input("Ingresa una lista de números separados por comas: ")

        lista_numeros = [inr(numero) for numero in entrada.spli (',')]
        pares, impares = contar_pares_impares(lista_numeros)
        print(f"Números pares: {pares}")
        print (f"Números impares: {impares}")

    except ValueError: 
        print("Por favor, ingresa una lista valida de numeros enteros separados por comas-")
