### Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.
muestra = input('Introduce una muestra de números separados por comas:')
numeros = [float(num) for num in muestra.split(",")]
media = sum(numeros) / len(numeros)
desviacion = (sum((x - media) ** 2 for x in numeros) / len(numeros)) ** 0.5
print(f'La media de la muestra es: {media:.2f}')
print(f'La desviación típica de la muestra es: {desviacion:.2f}')