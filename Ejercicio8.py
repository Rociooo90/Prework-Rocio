#Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def main():
    #Solicitar al usuario que ingrese su peso en kilogramos y su altura en metros
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))

    #Calcular el IMC usando la función calcular_imc
    imc = calcular_imc(peso, altura)

    #imprimir el resultado del IMC
    print(f"Tu índice de masa corporal es: {imc:.2f}")
