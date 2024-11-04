### Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
Palabra = input('Escribe una palabra')
if Palabra == Palabra[::-1]:
    print ('si')
else:
    print ('no')