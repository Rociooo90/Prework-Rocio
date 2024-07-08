"""Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros."""

def dolares_a_euros(dolares)
    tipo_cambio = 0.85
    euros = dolares * tipo_cambio

    return euros

def main()
    #Solicitar al usuario que diga los dólares a convertir
    dolares = float(input("Ingrese la cantidad de dólares a convertir a euros: "))

    euros = dolares_a_euros(dolares)

    print(f"{dolares} dólares son aproximadamente {euros:.2f} euros.")



