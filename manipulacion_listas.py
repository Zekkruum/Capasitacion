def multiplos_de_n(lista, n):
    return [numero for numero in lista if numero % n == 0]

# Ejemplo de uso
numeros = [5, 12, 8, 20, 7]
n = 4
resultado = multiplos_de_n(numeros, n)
print("Múltiplos de", n, ":", resultado)