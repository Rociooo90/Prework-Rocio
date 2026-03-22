# Ejercicio 1 contar caracteres. Crea una funcion para contar caracteres en cadenad de texto.

def contar_caracteres (texto):
    return len (texto)
# Ejemplo uso
texto= "hOLA Rocio" 
print("El texto tiene", contar_caracteres(texto))


# Ejercicio 2 Calcular promedio. Función calcule el promedio de una lista de números.

def calcular_promedio (lista_numeros):
        return sum(lista_numeros) / len (lista_numeros)
#Ejemplo de uso
numeros = [1,2,3,4,5,6,7,8]
print ("El promedio es:", calcular_promedio(numeros))


#Ejercicio 3 Encontrar duplicado. Funcion para encontrar el primer elemento duplicado de una lista.

def primer_duplicado(lista):
      elementos_vistos = set ()
      for elemento in lista:
            if elemento in elementos_vistos:
                return elemento
            elementos_vistos.add(elemento)
      return None
#Ejemplo
numeros = [2,3,4,5,3,4,5]
print("El primer duplicado es:", primer_duplicado(numeros))

#Ejercicio 4. enmascarado_datos. Funcion convierta variable en cadena de texto y enmascare todos los datos con # excepto los ultimos cuatro

def enmascarado_datos  (cadena):
      if len(cadena) <=4:
            return cadena
      return texto == "#" * (len(cadena)-4) + cadena[-4:]
#ejemplo pero da error
texto = "analistadedatos"
print(enmascarado_datos(texto))  

#Ejercicio 5. Funcion es_anagrama.  Crea una funcion para ver si dos palabras son anagramas.

def son_anagramas(palabra1, palabra2):
      return sorted(palabra1.lower()) == sorted(palabra2.lower())
#ejemplo pero da error 
print(son_anagramas("amor","roma"))


#Ejercicio 6.Funcion buscar_nombre- 

def buscar_nombre():
    #solicitar lista de nombres
    nombres = input("Ingrese una lista de nombres separados por comas: ")
    nombres = [nombre.strip().lower() for nombre in nombres.split(',')]
    #solicitar nombre a buscar
    nombre_buscar = input("Ingrese el nombre a buscar: ").strip().lower()
    #buscar y mostrar resultado
    if nombre_buscar in nombres:
           print(f"El nombre '{nombre_buscar}' fue encontrado en la lista.")
    else:
        raise ValueError(f"El nombre '{nombre_buscar}' no se encuentra en la lista.")

#Ejemplouso da error         
nombres = "Jaime","Silvia","Ana"
print(buscar_nombre)



#Ejercicio7.Funcion Fibonacci. Crea una funcion que calcule el termino n de la serie  de Fibonacci utilizando recursion.
def fibonacci (n):
    if n  <= 0:
         return "El indice debe ser un entero positivo" 
    elif n == 1:
         return 0
    elif n == 2:
         return 1
    else:
         return fibonacci(n-1) + fibonacci(n-2)
    
#ejemplodeuso
print(fibonacci(9))
print(fibonacci(10))


#Ejercicio8- encontrar_puesto_empleado. 
def buscar_puesto(nombre_completo, empleados):
     for empleado in empleados:
          if empleado ['nombre'].lower() == nombre_completo.lower():
               return empleado['puesto']
     return f"{nombre_completo} no trabaja aquí"

#ejemplodeuso
empleados = [
     {'nombre':'Juan Garcia','puesto': 'secretario'},
     {'nombre':'Mabel Garcia', 'puesto': 'ProducT Manager'},
     {'nombre':'Isabel Martin', 'puesto': 'CEO'}
]
print (buscar_puesto('Mabel Garcia', empleados))


#Ejercicio 9 -cubo_numero usando lambdas. Crea una funcion que calcule el cubo de un número dado mediante una función lambda-
factorial = lambda n: 1 if n == 0 else n * factorial (n-1)

#ejemplo de uso
print(factorial(5))


#Ejercicio 10- resto_division Usando lambdas. 
resto = lambda a, b: a % b

#ejemplo de uso
print(resto(17,5))


#Ejercicio 11. Funcion numeros pares usando lambdas y filter.
filtrar_pares = lambda lista: list (filter (lambda x: x % 2 == 0,lista))

#jemplo de uso 
numeros = [24,56,2.3,19,-1,0]
print(filtrar_pares(numeros))


#Ejercicio 12- Funcion numeros suma usando lambdas  y map:
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

#ejemplo de uso
lista_numeros1 = [24,56,2.3,19,-1,0]
print(sumar_tres(lista_numeros1))


#Ejercicio13 - Funcion sumar_listas usando lambdas. Funcion que sume elementos de dos listas
sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

#ejemplodeuso
lista_numeros1 = [1,4,5,6,7,7]
lista_numeros2 = [3,11,34,56]
print(sumar_listas(lista_numeros1, lista_numeros2))


#Ejercicio 14. No te vayas por las ramas. Crea la clase
#Arbol , define un árbol genérico con un tronco y ramas como atributos. Los
#métodos disponibles son: crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e
#info_arbol . El objetivo es implementar estos métodos para manipular la
#estructura del árbol.

class Arbol: 
     def __init__(self):
          self.tronco = 1
          self.ramas = []
     def crecer_tronco (self):
          self.tronco +=1
     def nueva_rama (self):
          self.ramas.append(1)
     def crecer_ramas(self):
          self.ramas = [rama + 1 for rama in self.ramas]
     def quitar_rama(self, posicion):
          if posicion < len(self.ramas):
               self.ramas.pop(posicion)
          else:
              print("Posicion invalida")
     def info_Arbol(self):
          info = f"Longitud del tronco: {self.tronco}\n"
          info += f"Numero de ramas; {len(self.ramas)}\n"
          info += "Longitudes de las ramas: "
          info += ", ".join(map(str, self.ramas))
          return info

#ejemplo de uso 
Arbol = Arbol ()
print (Arbol.info_Arbol())

Arbol.crecer_tronco(1)
Arbol.nueva_rama(1)
Arbol.crecer_ramas(1)
Arbol.nueva_rama(2)
Arbol.quitar_rama(2)
print (Arbol.info_arbol())


#Ejercicio 15 - Clase Usuario Banco. 

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
         self.nombre = nombre
         self.saldo = saldo 
         self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad): 
        if cantidad <= 0:
             raise ValueError ("La cantidad a retirar debe ser positiva")
        if cantidad > self.saldo:
             raise ValueError ("No hay suficiente saldo")
        self.saldo -= cantidad
        print(f"Se han retirado {cantidad} euros. Saldo actual: {self.saldo} euros")

    def transferir_dinero(self, otro_usuario, cantidad):
         if cantidad <=0:
              raise ValueError ("La cantidad a transferir debe ser positiva")
         if cantidad > otro_usuario.saldo:
              raise ValueError ("El otro usuario no tiene suficiente saldo")
         otro_usuario.saldo -= cantidad
         self.saldo += cantidad
         print(f"Se han transferido {cantidad} euros desde {otro_usuario.nombre}. Saldo actual: {self.saldo} euros")

    def agregar_dinero(self, cantidad):
         if cantidad <= 0:
              raise ValueError("La cantidad a agregar debe ser positiva")
         self.saldo += cantidad 
         print(f"Se han agregado {cantidad} euros. Saldo actual: {self.saldo} euros")

    def __str__(self):
        return f"Nombre: {self.nombre}\nSaldo: {self.saldo} euros\nCuenta corriente: {'Si' if self.cuenta_corriente else 'No'}"
    
#Ejemplo de uso.
Usuario1 = UsuarioBanco("Alicia",100, True)
Usuario2 = UsuarioBanco("Bob",50,True)

print(Usuario1)
print(Usuario2)

Usuario1.agregar_dinero(20)
Usuario2.transferir_dinero(Usuario1,80)
Usuario1.retirar_dinero(50)

print(Usuario1)
print(Usuario2)

#Ejercicio 16 ---- Funcion Procesar texto. 

def contar_palabras(texto):
     palabras = texto.split()
     conteo = {}
     for palabra in palabras:
          palabra = palabra.lower()
          if palabra in conteo:
               conteo[palabra] +=1
          else:
               conteo [palabra] = 1
     return conteo

def reemplazar_palabra(texto, palabra):
     return texto.replace (original, nueva)

def eliminar_palabra(texto, palabra): 
     palabras = texto.split()
     palabras = [p for p in palabras if p.lower() != palabra.lower()]
     return ''.join(palabras)

def procesar_texto(texto, opcion, *args):
     if opcion == 'contar':
          if len (args) !=0:
               raise ValueError ("La opcion 'contar' no requiere argumentos adicionales")
          return contar_palabras (texto)
     elif opcion == 'reemplazar':
        if len (args) !=2:
             raise ValueError ("La opcion 'reemplazar' requiere dos argumentos: la palabra original y la nueva palabra")
        original, nueva = args
        return reemplazar_palabra(texto, original, nueva)
     elif opcion == 'eliminar':
          if len (args) !=1:
               raise ValueError ("La opcion 'eliminar' requiere dos argumentos: la palabra original y la nueva palabra")
          palabra = args [0]
          return eliminar_palabra (texto, palabra)
     else:
          raise ValueError("Opcion invalida. Las opciones son: 'contar', 'reemplazar', 'eliminar'")

#Ejemplo de uso 
texto = "Este es un ejemplo de texto. Este texto contiene palabras repetidas."

print ("Contar palabras:")
print (procesar_texto(texto, 'contar'))

print ("\nReemplazar 'texto' por 'relato':")
print (procesar_texto(texto, 'reemplazar', 'texto', 'relato'))

print ("\nEliminar la palabra 'ejemplo':")
print (procesar_texto(texto, 'eliminar', 'ejemplo'))