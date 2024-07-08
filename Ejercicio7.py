"""
Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario"""

def suma(a, b):
        return a + b

def resta(a, b):
        return a - b

def multiplicacion(a, b):
        return a * b

def division(a, b):
        if b != 0:
                return a / b
        else:
                return "Error: Division por cero no permitida"
        

def menu():
        print("Selecciona la operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")

def manin():
        while True:
            menu()
            eleccion = input("Intrdoduce el número de la operación que deseas realizar (1/2/3/4) o 'q' para salir: ")

            if eleccion == 'q':
                print("Saliendo del programa. ¡Adiós!")
                break

            if eleccion in ['1','2','3','4',]:
                   num1 = float(input("Introduce el primero numero: "))
                   num2 = float(input("Intoduce el segundo número: "))

                   if eleccion == '1':
                        print(f"Resultado: {suma(num1, num2)}")
                   elif eleccion == '2':
                        print(f"Resultado: {resta(num1, num2)}") 
                   elif eleccion == '3':
                        print(f"Resultado: {multiplicacion(num1, num2)}")
            else:
                print("Opcion no válida. Por favor, elige una opcion del 1 al 4")  
                                   