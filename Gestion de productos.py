class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def valor_total_stock(self):
        return self.cantidad * self.precio

class inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self):
        print("\n" + "=" * 40)
        nombre = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        producto = Producto(nombre, cantidad, precio)
        self.productos.append(producto)
        print("Producto agregado correctamente.")

    def buscar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre.lower() == nombre_producto.lower():
                return producto
        return None
    
    def calcular_valor_total_inventario(self):
        return sum(producto.valor_total_stock() for producto in self.productos)
       
    

def app():
    agregar_producto = inventario()  

    while True:
        print("\n" + "=" * 40)
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Mostrar productos")
        print("5. Valor total del inventario")
        print("6. Salir") 
        print("\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto.agregar_producto()
        elif opcion == "2":
            if agregar_producto.productos:
                for producto in agregar_producto.productos:
                    print(producto.mostrar_info())
            else:
                print("No hay productos en el inventario.")
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a buscar: ")
            producto_encontrado = agregar_producto.buscar_producto(nombre_producto)
            if producto_encontrado:
                print(producto_encontrado.mostrar_info())
                print(f"Valor total en stock: {producto_encontrado.valor_total_stock()}")
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            if agregar_producto.productos:
                for producto in agregar_producto.productos:
                    print(producto.mostrar_info())
            else:
                print("No hay productos en el inventario.")
        elif opcion == "5":
            valor_total = agregar_producto.calcular_valor_total_inventario()
            print(f"Valor total del inventario: {valor_total}")
        
        elif opcion == "6":
            print("Saliendo de la aplicación.")
            break

        else:
            print("Opción no válida, intente de nuevo.")

app()