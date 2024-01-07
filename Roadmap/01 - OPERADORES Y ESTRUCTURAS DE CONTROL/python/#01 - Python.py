#Ejemplos con todos los operadores de Python. 

# Operadores Aritméticos 
print(10 + 2) #12
print(11 - 2) #9
print(12 * 2) #24
print(13 / 2) #6.5
print(14 % 2) #0
print(15 ** 2) #225
print(16 // 2) #8

# Operadores de Asignación.
# Guarda el valor de la primera variable y realiza la operación. En paralelo podemos agregarle un nuevo valor para que nos devuelva otro resultado.

# "+=" para hacer incremento a una variable
x=5
x+=1 
print(x) #6

# "*=" para multiplicar una variable
x= 'Hola'
x*=3 
print(x) #HolaHolaHola

# "**=" para hacer potenciaciones 
x=5 
x**=5 
print(x) #3125

# Asi mismo, están para los demás operadores aritmeticos. "-=", "/=", "%=", "//=". 


# Operadores Relacionales 
x = 4
y = 5 
print(x > y) #False

x = 5
y = 5 
print(x == y) #True

x = 4
y = 5 
print(x != y) #True

x = 5 
y = 4 
print(x <= y) #False


# Operadores Lógicos
print(True and False) #False

print(True or False) #True

print(not False) #True

print(True and True and False) #False

# Operadores Bitwise o a nivel de Bit. Operaciones logicas con Bits. 

# Operador "&". Si ambos bits son 1, el resultado es 1. Si no se cumple esta condición el resultado será 0.
variable1 = 10  # Representación binaria: 1010
variable2 = 12  # Representación binaria: 1100
print(bin(variable1 & variable2)) #0b1000 (representación binaria del 8)
"""" Mas o menos asi se ve la operación 
      1010  (variable1)
    & 1100  (variable2)
      ----
      1000  (resultado en binario) que representa a su vez el numero 8"""

# Operador "|". Si al menos uno de los bits es 1, el resultado es 1. Si ambos bits son 0, el resultado es 0.
variable1 = 10  #Representación binaria: 1010
variable2 = 5   #Representación binaria: 0101
""" 
   1010  (variable1)
 | 0101  (variable2)
   ----
   1111  (resultado en binario)
"""
print(bin(variable1 | variable2)) #0b1111: Representa el número 15.

# Operador "^". El resultado es 1 si los bits son diferentes y 0 si son iguales.
variable1 = 10  #Representación binaria: 1010
variable2 = 5   #Representación binaria: 0101
""" 
   1010  (variable1)
 ^ 0101  (variable2)
   ----
   1111  (resultado en binario)
"""
print(bin(variable1 ^ variable2)) #0b1111: Representa el número 15.

# Operador "~". Invierte cada bit en el número. Cambia 1 a 0. Y 0 a 1.
variable1 = 10  #Representación binaria: 1010
""" 
  ~1010  (variable1)
   ----
   0101  (resultado en binario)
""" 
print(bin(~variable1)) #-0b1011 representa el número -5

# Operadores de identidad 
a = 10
b = 10
print(a is b) #True. Apuntan al mismo objeto "10"

a = 10
b = 10
print(a is not b) #False. Se pregunta si A y B no son el mismo objeto.

# Operadores de membresía
print(3 in [1, 2, 3])
#True

print(3 not in [1, 2, 4, 5])
# True

# Operador Walrus
print(x := "Python")








# Operaciones que representen estructuras de control

# Condicional if 
a = 4
b = 2
if b != 0: #si b es distinto a 0, haz la division de enteros a//b
    print(a//b)

# Condicional else
x = 10
if x == 5:#si x es igual a 5
    print("Es 5") #imprime: "es 5"
else:
    print("No es 5") #si no se cumple, imprime "No es 5"

# Condicional elif
x = 7
if x == 5: #si x es igual a 5
    print("Es 5") 
    #imprime: "es 5"
elif x == 6: #si x es igual a 6
    print("Es 6") 
    #imprime: "es 6"
elif x == 7: #si x es igual a 7
    print("Es 7") 
    #imprime: "es 7"
else: #si ninguna de las anteriores se cumple
    print("Es otro") 
    #imprime "es otro"

# Bucle for
for i in range(0, 5):
    print(i)

diccionario = {"a": 1, "b": 2, "c": 3}
for clave, valor in diccionario.items():
  print(clave, valor)

# Bucle while 
x = 5
while x > 0:
    x -=1
    print(x)

x = 5
while x > 0:
    x -=3
    print(x) #2, -1
else:
    print("El bucle ha finalizado")

# Condicional Break para finalizar bucles
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra) #P, y, t, Se encontró la h

x = 5
while True:
    x -= 1
    print(x)
    if x == -1:
        break
    

# Condicional Continue, salta lo que se asigne
cadena = 'Python'
for letra in cadena:
    if letra == 't':
        continue
    print(letra) #P, y, h, o, n 

cadena = "Hola"
for c in cadena:
    print(c)




#Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.