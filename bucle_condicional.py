while True:
    entrada = input("Ingrese un número entero positivo: ")
    try:
        numero = int(entrada)
        if numero > 0:
            print("Número válido ingresado:", numero)
            break
        else:
            print("Error: El número debe ser mayor que 0.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")