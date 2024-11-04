### Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
Palabra = input('Escribe una palabra')
if Palabra == Palabra[::-1]: ### el reversed no me funciona esto es lo mismo pero mejor. :)
    print ('Si es un palíndromo')
else:
    print ('No es un palíndromo')