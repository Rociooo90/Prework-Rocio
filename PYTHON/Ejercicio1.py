'''Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.'''

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius*9/5)+32
    return fahrenheit
celsius = float(input("Ingrese la tempertura en grados Celsius:"))
fahrenheit = celsius_a_fahrenheit(celsius) 
print(f"{celsius}") "grados_celsius_son {fahrenheit} grados_fahrenheit".










