"""Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos."""

def convertir_minutos (minutos_totales):
    horas = minutos_totales // 60 
    minutos = minutos_totales % 60 
    return horas, minutos

def main():
    try:
        minutos_totales = int(input("Ingresa el número de minutos: "))
        horas, minutos = convertir_minutos(minutos_totales)
        print(f"{minutos_totales} minutos son {horas} horas y {minutos} minutos.")
    
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
