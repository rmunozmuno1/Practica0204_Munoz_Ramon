### Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
lista = ['Dapi', 'Sirc', 'Sihd']
Nota_Dapi = float(input('¿Que nota has sacado en dapi'))
Nota_Sirc = float(input('¿Que nota has sacado en Sirc'))
Nota_sihd = float(input('¿Que nota has sacado en Sihd'))
Notas = [Nota_Dapi, Nota_Sirc, Nota_sihd]
print ('En', lista[0], 'he sacado', Notas[0])
print ('En', lista[1], 'he sacado', Notas[1])
print ('En', lista[2], 'he sacado', Notas[2])