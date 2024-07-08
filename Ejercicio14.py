"""Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%."""

def calcular_precio_final(precio_inicial, descuento):
    precio_final = precio_inicial - (precio_inicial * descuento/100)
    return precio_final

def main():
    try:
        precio_inicial = float(input("Ingresa el precio inicial del artículo: "))
        descuento = 20 #Descuento del 20%
        precio_final = calcular_precio_final(precio_inicial, descuento)
        print(f"El precio final después de aplicar un {descuento} % de descuento es: ${precio_final:.2f}")
    
    except ValueError:
        print("Por favor, ingresa un valor número válido para el precio.")


