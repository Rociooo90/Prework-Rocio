"""Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo."""

def calcular_area_rectangulo(longitud, ancho):
    area = longitud * ancho
    return area

def main():
    #Solicitar al usuario que ingrese la longitud y el ancho del rectángulo
    longitud = float(input("Ingrese la longitud del rectángulo: "))
    ancho = float(input("Ingresa el ancho del rectángulo: "))
