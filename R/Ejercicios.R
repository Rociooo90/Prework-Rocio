#Ejecicio 1: Define una variable llamada numero con el valor 10 y otra llamada
#nombre con tu nombre.
numero <- 10
nombre <- "Rocio"

#-----

#Ejercicio 2: Utiliza las funciones class e is.numeric para determinar el tipo de
#dato de numero .
numero <- 10
# Determinar la clase del dato
print(class(numero))  

# Verificar si es un número
print(is.numeric(numero))  

#-----

#Ejercicio 3: Realiza una operación aritmética que sume numero y el doble de
#numero.
numero <- 10
resultado <- numero + (2 * numero)  # Sumar numero con su doble
print(resultado)

#-----

#Ejercicio 4: Crea un vector llamado edades con las edades de tres personas y
#una lista llamada informacion con el nombre y la edad de una persona

edades <- c(25, 30, 40)

# Crear una lista llamada 'informacion' con el nombre y la edad de una persona

informacion <- list(nombre = "Carlos", edad = 30)

print(edades)
print(informacion)

#-----

#Ejercicio 5:Enunciado: Verifica si nombre es de tipo caracter y si es_numerico es de tipo
#lógico
nombre <- "Rocío"
es_numerico <- TRUE

# Verificar si 'nombre' es de tipo carácter
print(is.character(nombre))  

# Verificar si 'es_numerico' es de tipo lógico
print(is.logical(es_numerico))  

#-----
  
#Ejercicio 6: Crea una variable llamada mayor_de_edad que sea TRUE si la edad
#de la primera persona en edades es mayor o igual a 18.  
  
edades <- c(25, 30, 40)

# Verificar si la primera persona es mayor de edad
mayor_de_edad <- edades[1] >= 18  

print(mayor_de_edad)

#-----
  
#Ejercicio 7:  Utiliza el operador %in% para verificar si el valor 30 está presente
#en el vector edades .
edades <- c(25, 30, 40)

# Verificar si 30 está en el vector
presente <- 30 %in% edades  

print(presente)

#-----
  
#Ejercicio 8:: Compara si el doble de numero es mayor que edades[3].
edades <- c(25, 30, 40)
numero <- 12  #Ej de número

doble_numero <- 2 * numero

resultado <- doble_numero > edades[3]
print(resultado)

#-----

#Ejercicio 9:Define dos variables lógicas, condicion1 y condicion2 , ambas con
#valor TRUE . Comprueba si ambas condiciones son verdaderas.
condicion1 <- TRUE
condicion2 <- TRUE

#Comprobación de si ambas condiciones son verdaderas
resultado <- condicion1 && condicion2

print(resultado)

#-----

#Ejercicio 10: Define una variable lógica, verdadero, con valor TRUE. Comprueba
#que su valor NO sea verdadero.

verdadero <- TRUE

# Comprobación de si el valor NO es verdadero
resultado <- !verdadero

print(resultado)
