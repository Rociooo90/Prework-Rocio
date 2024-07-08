"""Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros."""

def convertir_millas_a_kilometros(millas):
    #1 milla es 1.60934 kilómetros
    kilometros = millas * 1.60934
    return kilometros

def main():
    try:
        millas = float(input("Ingresa la distancia en millas: "))
        if millas < 0:
            print("Por favor, ingresa una distancia positiva.")
        
        else:
            kilometros = millas_a_kilometros(millas)
            print(f"{millas} millas equivalen a {kilometros:.2f} kilómetros.")
    except ValueError:
        print("Por favor, ingresa un número válido para la distancia en millas")

