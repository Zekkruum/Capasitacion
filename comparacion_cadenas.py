def son_anagramas(cadena1, cadena2):
    c1 = sorted(cadena1.replace(" ", "").lower())
    c2 = sorted(cadena2.replace(" ", "").lower())
    return c1 == c2

# Ejemplos de uso
print(son_anagramas("Roma", "Amor"))               # True
print(son_anagramas("Hola", "Adiós"))              # False
print(son_anagramas("La cosa", "Sacola"))          # True