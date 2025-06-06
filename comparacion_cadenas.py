def son_anagramas(cadena1, cadena2):
    c1 = sorted(cadena1.replace(" ", "").lower())
    c2 = sorted(cadena2.replace(" ", "").lower())
    return c1 == c2
    
print(son_anagramas("Roma", "Amor"))               
print(son_anagramas("Hola", "Adiós"))              
print(son_anagramas("La cosa", "Sacola"))          
