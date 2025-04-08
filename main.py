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
CATEGORIAS = ["Electronica", "Ropa", "Alimentos", "Hogar", "Juguetes", "Calzado", "Decoracion", "Aseo", "Lacteos"]  # Categorías de productos
CATEGORIAS_lower = ["electronica", "ropa", "alimentos", "hogar", "juguetes", "calzado", "decoracion", "aseo", "lacteos"]  # Categorías de productos
inventario = {}
contador_id = 5

def autenticar():
    usuario = input("Usuario: ")
    contraseña = getpass.getpass("Contraseña: ")
    if USUARIOS.get(usuario) == contraseña:
        logging.info(f"Usuario {usuario} autenticado correctamente.")
        print("Acceso concedido.")
        return True
    logging.warning(f"Intento fallido de autenticación para usuario {usuario}.")
    print("Usuario o contraseña incorrectos.")
    return False

def agregar_producto():
    global contador_id
    try:
        nombre = input("Nombre del producto: ")
        if not nombre:
            logging.warning("Intento de agregar producto sin nombre.")
            print("Error: El nombre no puede estar vacío.")
            return
        descripcion = input("Descripción: ")
        cantidad = int(input("Cantidad disponible: "))
        if cantidad <= 0:
            logging.warning("Intento de agregar producto con cantidad no válida.")
            print("Error: La cantidad debe ser mayor a cero.")
            return
        precio = float(input("Precio unitario: "))
        if precio <= 0:
            logging.warning("Intento de agregar producto con precio no válido.")
            print("Error: El precio debe ser mayor a cero.")
            return
        categoria = input(f"Categoría ({', '.join(CATEGORIAS)}): ")
        if categoria.lower() not in CATEGORIAS_lower:
            print("Error: Categoría inválida.")
            logging.error("Intento de agregar producto con categoría inválida.")
            return
        sku = f"SKU{contador_id:04d}"
        inventario[contador_id] = {"nombre": nombre, "descripcion": descripcion, "cantidad": cantidad, "precio": precio, "categoria": categoria[0].upper() + categoria[1:].lower(), "sku": sku}
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
        print(f"ID: {id}, SKU: {producto['sku']}, Nombre: {producto['nombre']}, Descripción: {producto['descripcion']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}, Categoría: {producto['categoria']}")
    logging.info("Consulta de productos realizada.")

def buscar_producto():
    filtro = input("Ingrese el nombre o la categoría del producto a buscar: ")
    resultados = [(id, producto) for id, producto in inventario.items() if filtro.lower() in producto['nombre'].lower() or filtro.lower() in producto['categoria'].lower()]
    if resultados:
        for id, producto in resultados:
            print(f"ID: {id}, SKU: {producto['sku']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}, Categoría: {producto['categoria']}")
        logging.info(f"{len(resultados)} producto(s) encontrados con el filtro '{filtro}'.")
    else:
        logging.warning(f"No se encontraron productos con el filtro '{filtro}'.")
        print("No se encontraron productos.")

def actualizar_producto():
    try:
        id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        if id_producto in inventario:
            nombre = input("Nuevo nombre (deje en blanco para mantener): ") or inventario[id_producto]['nombre']
            descripcion = input("Nueva descripción: ") or inventario[id_producto]['descripcion']
            cantidad = int(input("Nueva cantidad: ") or inventario[id_producto]['cantidad'])
            if cantidad < 0:
                logging.warning("Intento de actualizar producto con cantidad no válida.")
                print("Error: La cantidad debe ser mayor o igual a cero.")
                return
            precio = float(input("Nuevo precio: ") or inventario[id_producto]['precio'])
            if precio <= 0:
                logging.warning("Intento de actualizar producto con precio no válido.")
                print("Error: El precio debe ser mayor a cero.")
                return
            categoria = input(f"Nueva categoría ({', '.join(CATEGORIAS)}): ") or inventario[id_producto]['categoria']
            if {categoria[0].upper() + categoria[1:].lower()} not in CATEGORIAS:
                print("Error: Categoría inválida.")
                logging.error("Intento de actualizar producto con categoría inválida.")
                return
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

def generar_reporte():
    cantidad_total = sum(producto['cantidad'] for id, producto in inventario.items())
    total_valor = sum(producto['cantidad'] * producto['precio'] for id, producto in inventario.items())
    agotados = [producto for id, producto in inventario.items() if producto['cantidad'] == 0]
    logging.info("Reporte generado.")
    print(f"Cantidad total de productos en inventario: {cantidad_total}")
    print(f"Valor total del inventario: ${total_valor:.2f}")
    agotados_string = ', '.join([f"{producto['nombre']}" for id, producto in inventario.items() if producto['cantidad'] == 0])
    print(f"Hay {len(agotados)} productos agotados: {agotados_string}.")

def menu():
    # Se agregan productos base para poblar el inventario.
    inventario[1] = {"nombre": "Laptop", "descripcion": "Laptop HP", "cantidad": 10, "precio": 500.0, "categoria": "Electronica", "sku": "SKU0001"}
    inventario[2] = {"nombre": "Camisa", "descripcion": "Camisa de algodón", "cantidad": 20, "precio": 25.0, "categoria": "Ropa", "sku": "SKU0002"}
    inventario[3] = {"nombre": "Leche", "descripcion": "Leche entera", "cantidad": 30, "precio": 1.5, "categoria": "Lacteos", "sku": "SKU0003"}
    inventario[4] = {"nombre": "Silla", "descripcion": "Silla de oficina", "cantidad": 15, "precio": 75.0, "categoria": "Hogar", "sku": "SKU0004"}
    logging.info("Sistema de inventario iniciado con 4 productos base.")
    while True:
        print("\n1. Agregar producto\n2. Consultar productos\n3. Actualizar producto\n4. Eliminar producto\n5. Actualizar stock\n6. Buscar producto\n7. Generar reporte.\n8. Salir.")
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
            buscar_producto()
        elif opcion == "7":
            generar_reporte()
        elif opcion == "8":
            logging.info("Usuario salió del programa.")
            break
        else:
            logging.warning(f"Selección de opción inválida: {opcion}")
            print("Opción inválida.")

if __name__ == "__main__":
    if autenticar():
        menu()
