# INF331-Tarea-1

### Integrantes: Bastián Gaete Aguilera - 201803008-2.

## Validación:
El requerimiento con el que se trabajará consistirá en lo siguiente:
Un emprendedor nos ha solicitado una aplicación para gestionar su inventario de productos en la bodega de su negocio. Este tendrá que utilizar la consola para las operaciones y las salidas de algunas de las opciones.

1. __CRUD de Productos:__ Permitir a los usuarios agregar, consultar, actualizar y eliminar productos del inventario. Cada producto debe tener un nombre, descripción, cantidad disponible, precio unitario y categoría (como Electrónica, Ropa, Alimentos).
2. __Gestión de Stock:__ Permitir actualizar la cantidad de productos cuando se vendan o se reciban nuevas unidades.
3. __Filtrado y Búsqueda:__ Opciones de filtrado de los productos en base a las categorías y búsqueda de los productos en base a palabras dentro del nombre del producto.
4. __Generación de Reportes:__ Mostrar un resumen con el total de productos en inventario, el valor total del inventario y los productos agotados. El reporte se entregará a través de la consola del programa.
5. __Autenticación:__ Proteger el acceso con un sistema de autenticación por nombre de usuario y contraseña.

Para validar de que estos requisitos se estén cumpliendo, se realizarán distintas pruebas probando cada una de las funcionalidades.

## Verificación:


## Supuestos realizados:
- No hay distintos roles para los usuarios.
- Los usuarios son creados por nosotros, y no por cada usuario del programa (lista de usuarios y contraseñas será incluida posteriormente).
- Las categorías de los productos son creadas por nosotros, se entregará una lista de estas posteriormente.
- El filtro solo consistirá en un filtro por la categoría de un producto. Mientras que el sistema de búsqueda será en base a palabras contenidas en los nombres de los productos.
- Cada ítem contará con un ID numérico generado automáticamente, además de un SKU específico.
- Un producto no puede tener stock negativo.
