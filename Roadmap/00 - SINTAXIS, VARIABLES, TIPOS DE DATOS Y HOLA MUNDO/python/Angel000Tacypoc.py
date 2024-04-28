#voy a usar 3 referencias bibliograficas, o 3 recursos que basicamente son lo mismo pero uno mas ordenado que el otro. 

"""
- Canal de youtube con varios tutoriales sobre python https://www.youtube.com/@SoloPython
- Documentación actualizada, ordenada y en español https://ellibrodepython.com/
- Documentación original https://docs.python.org/3.12/contents.html
"""

#Formas de hacer comentarios
Los comentarios se inician con "#" y todo lo que vaya después en la misma línea será considerado un comentario.

Tambien se puede crear un comentario en diferentes lineas o con espaciado usando las triple comillas: """ """

#Creacion de una Variable
Una de las ventajas de python es que no se necesita declararlas antes. Solo asignandoles valor ya se hace una variable. Siempre y cuando no se usen las palabras reservadas de Python ni espacios, guiones o números al principio.
Ejemplo: 
h = 6
k = 10 
x, y, z = 15, 20, 30
Me_Llamo = "Luis" 

#Resultados de las variables en pantalla
print (h) #6
print (k) #10 
print (z) #30
print (x) #15

""" Sintaxis No validas para declarar variables ""
  2variable = 10
  var-iable = 10
  var iable = 10
""" 

""" Variables segun tipo de datos 
  Entero o Int
  Booleano
  Float
  Números complejos
  Cadenas o strings
"""


#Int 
import sys  # import sys es un módulo que proporciona variables y funciones relacionadas con el sistema, como la memoria y la ejecución del código.
i = 5 
print (i) #Resultado de consola = 5
print(sys.getsizeof(i), type(i)) #Resultado de consola = "28" que es el tamaño de la variable en bytes o memoria. Y el tipo de variable que es i=5: "<class 'int'>"







#Booleanos
  #Pasa de que en python necesitas tirar un print e indicar una operacion o evulizacion de una expresion para que sea vista en consola. Por ejemplo: 
print(2 > 1)
print(1 <= 0)

#Tambien existe una funcion llamada Bool con la que puedes sacar un booleano de un valor 
print(bool(10)) 
print(bool([]))    

#Pero tambien se pueden usar varoles para realizar operaciones logicas
a = True
b = False

C = a and b
D = a or b

print(C)
print(D)







#Float 
  #permite representar un número con decimales positivo o negativo, es decir, numeros reales.
f = 0.10093
print(f) #Resultado: 0.10093
print(type(f)) #Resultado: <class 'float'>









#Numeros complejos
""" son aquellos que tienen dos partes:
 * Una parte con numeros reales, como por ejemplo 3 o 7.5
 * Y otra "imaginaria", como 5j o -7j
  los números imaginarios son números reales acompañados de la constante i (a veces la j es usada indistintamente) """

a = 5 + 5j #Numero real + Parte imaginaria 
b = 1.3 - 7j #Numero real + Parte imaginaria 
print(a, b)
#Resultado a=(5+5j) b=(1.3-7j)

c = 3 + 5j
print(c) #(3+5j)
print(type(c)) #<class 'complex'>

c = 3 + 5j
print(c.real) #3.0
print(c.imag) #5.0





#Cadenas de texto o strings 
 #Para crear un string o cadena de texto se hace uso de una variable que incluya comillas dobles o comilla simples entre el texto a exponer. 
s = "Esto es una cadena"
print(s) #Resultado: Esto es una cadena
print(type(s)) #Resultado: <class 'str'>

#Una cadena puede estar también vacía.
s = ''
print(s)

#Incrustacion de comillas dentro de una cadena
s = "\"Esto es una comilla doble\" de ejemplo"
print(s) #Resultado: "Esto es una comilla doble" de ejemplo

#Tambien se pueden hacer saltos de línea (como el enter) dentro de una cadena
s = "Primer linea\nSegunda linea"
print(s) 
#Resultado: 
#Primer linea
#Segunda linea






#Listas 
 #Son como los array en otros lenguajes de programación. Permite almacenar un conjunto arbitrario de datos. Se puede guardar en ellas prácticamente lo que sea.
lista = [1, 2, 3, 4]
print(lista[1]) #Resultado: 2

a = [90, "Python", 3.87, 4.5, "Lu"]
print(a[0]) #Resultado: 90
print(a[1]) #Resultado: Python
print(a[2]) #Resultado: 3.87
#Se puede acceder directamente al ultimo agregando un -1 y al penultimo con el -2 y asi sucesivamente
print(a[-1]) #Resultado: Lu
#Se pueden hacer operaciones entre numeros. 
print(a[0] -1) #Resultado: 89
print(a[2]*5) #Resultado: 19.35

#un pequeño ejercicio :)
# Nombre del Arbol = Pino
# Tipo de arbol = Conífero
# Altura del arbol = 20
# Edad del arbol = 100

arboles = [['Pino', 'Conífero', 20, 100]]

arbol, tipo_arbol, nombre_arbol, altura_arbol, edad_arbol = arboles[0], arboles[0][1], arboles[0][0], arboles[0][2], arboles[0][3]
print(arbol)
print(tipo_arbol, nombre_arbol, altura_arbol, edad_arbol)









#Orden de MoureDev
p = '¡Hola, Python!'
print(p)