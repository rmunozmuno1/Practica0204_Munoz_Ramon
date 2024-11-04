# Almacenar el abecedario en una lista
abecedario = list("abcdefghijklmnopqrstuvwxyz")
abecedario2 = [letra for i, letra in enumerate(abecedario, start=1) if i % 3 != 0]
print("Lista del abecedario sin posiciones múltiplos de 3:")
print(abecedario2)