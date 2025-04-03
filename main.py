import json
import getpass
import logging

# Configuración del sistema de logs
logging.basicConfig(
    filename='inventario.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Datos predefinidos
USUARIOS = {"admin": "1234"}  # Diccionario de usuarios y contraseñas
CATEGORIAS = ["Electrónica", "Ropa", "Alimentos"]
inventario = {}
contador_id = 1

def autenticar():
    usuario = input("Usuario: ")
    contraseña = getpass.getpass("Contraseña: ")
    if USUARIOS.get(usuario) == contraseña:
        logging.info(f"Usuario {usuario} autenticado correctamente.")
        print("Acceso concedido.")
        return True
    logging.warning(f"Intento fallido de autenticación para usuario {usuario}.")
    print("Acceso denegado.")
    return False

def agregar_producto():
    global contador_id
    try:
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción: ")
        cantidad = int(input("Cantidad disponible: "))
        precio = float(input("Precio unitario: "))
        categoria = input(f"Categoría ({', '.join(CATEGORIAS)}): ")
        if categoria not in CATEGORIAS:
            print("Categoría inválida.")
            logging.error("Intento de agregar producto con categoría inválida.")
            return
        sku = f"SKU{contador_id:04d}"
        inventario[contador_id] = {"nombre": nombre, "descripcion": descripcion, "cantidad": cantidad, "precio": precio, "categoria": categoria, "sku": sku}
        contador_id += 1
        logging.info(f"Producto agregado: {nombre} (ID: {contador_id - 1}, SKU: {sku})")
        print("Producto agregado con éxito.")
    except ValueError as e:
        logging.error(f"Error al ingresar datos numéricos en agregar_producto(): {e}")
        print("Error: Ingrese valores numéricos válidos.")

def consultar_productos():
    if not inventario:
        print("No hay productos en el inventario.")
    for id, producto in inventario.items():
        print(f"ID: {id}, SKU: {producto['sku']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}, Categoría: {producto['categoria']}")
    logging.info("Consulta de productos realizada.")

def actualizar_producto():
    try:
        id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        if id_producto in inventario:
            nombre = input("Nuevo nombre (deje en blanco para mantener): ") or inventario[id_producto]['nombre']
            descripcion = input("Nueva descripción: ") or inventario[id_producto]['descripcion']
            cantidad = int(input("Nueva cantidad: ") or inventario[id_producto]['cantidad'])
            precio = float(input("Nuevo precio: ") or inventario[id_producto]['precio'])
            categoria = input(f"Nueva categoría ({', '.join(CATEGORIAS)}): ") or inventario[id_producto]['categoria']
            inventario[id_producto].update({"nombre": nombre, "descripcion": descripcion, "cantidad": cantidad, "precio": precio, "categoria": categoria})
            logging.info(f"Producto actualizado: {nombre} (ID: {id_producto})")
            print("Producto actualizado con éxito.")
        else:
            logging.warning(f"Intento de actualizar producto con ID inexistente: {id_producto}")
            print("ID no encontrado.")
    except ValueError as e:
        logging.error(f"Error al ingresar datos numéricos en actualizar_producto(): {e}")
        print("Error: Ingrese valores numéricos válidos.")

def eliminar_producto():
    try:
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
        if id_producto in inventario:
            del inventario[id_producto]
            logging.info(f"Producto eliminado (ID: {id_producto})")
            print("Producto eliminado.")
        else:
            logging.warning(f"Intento de eliminar producto con ID inexistente: {id_producto}")
            print("ID no encontrado.")
    except ValueError as e:
        logging.error(f"Error al ingresar datos numéricos en eliminar_producto(): {e}")
        print("Error: Ingrese un ID válido.")

def actualizar_stock():
    try:
        id_producto = int(input("Ingrese el ID del producto: "))
        if id_producto in inventario:
            cantidad = int(input("Ingrese cantidad a agregar (+) o vender (-): "))
            nueva_cantidad = inventario[id_producto]['cantidad'] + cantidad
            if nueva_cantidad < 0:
                logging.warning(f"Intento de establecer stock negativo para ID {id_producto}")
                print("Error: No puede haber stock negativo.")
            else:
                inventario[id_producto]['cantidad'] = nueva_cantidad
                logging.info(f"Stock actualizado para ID {id_producto}, nueva cantidad: {nueva_cantidad}")
                print("Stock actualizado.")
        else:
            logging.warning(f"Intento de actualizar stock con ID inexistente: {id_producto}")
            print("ID no encontrado.")
    except ValueError as e:
        logging.error(f"Error al ingresar datos numéricos en actualizar_stock(): {e}")
        print("Error: Ingrese valores numéricos válidos.")

def menu():
    while True:
        print("\n1. Agregar producto\n2. Consultar productos\n3. Actualizar producto\n4. Eliminar producto\n5. Actualizar stock\n6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            actualizar_stock()
        elif opcion == "6":
            logging.info("Usuario salió del programa.")
            break
        else:
            logging.warning(f"Selección de opción inválida: {opcion}")
            print("Opción inválida.")

if __name__ == "__main__":
    if autenticar():
        menu()
