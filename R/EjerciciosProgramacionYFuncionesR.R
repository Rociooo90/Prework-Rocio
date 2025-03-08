#Ejercicio1: Define una función llamada saludo que imprima en la consola el
#mensaje "Hola, bienvenido a R".

saludo <- function() {print("Hola, bienvenido a R")}

saludo()

#Ejercicio2:Crea una función llamada calificar_edad que tome un parámetro
#numérico llamado edad y muestre en la consola si la persona es "menor de
#edad" o "mayor de edad"

calificar_edad <- function(edad) {
  if (edad < 18) {
    print("Menor de edad")
  } else {
    print("Mayor de edad")
  }
}

# Ejemplos
calificar_edad(15)
calificar_edad(20)  


#Ejercicio3:Define una función llamada tabla_multiplicar que tome un
#parámetro numérico n e imprima la tabla de multiplicar del 1 al 10 de ese
#número.

tabla_multiplicar <- function(n) {
  for (i in 1:10) {
    print(paste(n, "x", i, "=", n * i))
  }
}

# Ejemplo 
tabla_multiplicar(5)

#Ejercicio4:Crea una función llamada numeros_pares que tome un parámetro
#numérico limite e imprima los números pares hasta ese límite.

numeros_pares <- function(limite) {
  for (i in 2:limite) {
    if (i %% 2 == 0) {
      print(i)
    }
  }
}

#Ejemplo
numeros_pares(10)

#Ejercicio5:Define una función llamada matriz_cuadrada que tome un parámetro
#numérico n e imprima una matriz cuadrada de tamaño n x n donde los
#elementos son el resultado de la suma de sus índices de fila y columna.

matriz_cuadrada <- function(n) {
  # Crear una matriz de tamaño n x n con ceros
  matriz <- matrix(0, nrow = n, ncol = n)
  
  # Llenar la matriz con la suma de los índices de fila y columna
  for (i in 1:n) {
    for (j in 1:n) {
      matriz[i, j] <- i + j
    }
  }
  
  print(matriz)
}

# Ejemplo
matriz_cuadrada(4)

