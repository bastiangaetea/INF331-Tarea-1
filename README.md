# INF331-Tarea-1

### Integrantes: Bastián Gaete Aguilera - 201803008-2.

## Instalación y Cómo usar
Se requiere tener Python 3 instalado.
Una vez instalado, moverse a la carpeta donde esta el archivo .py y ejecutar lo siguiente:
```
python main.py
```
Esto ejecutará el programa y quedará desplegado el menú con el que se puede empezar a añadir productos, actualizarlos, eliminarlos, etcétera.

## Validación:
El requerimiento con el que se trabajará consistirá en lo siguiente:
Un emprendedor nos ha solicitado una aplicación para gestionar su inventario de productos en la bodega de su negocio. Este tendrá que utilizar la consola para las operaciones y las salidas de algunas de las opciones.

1. __CRUD de Productos:__ Permitir a los usuarios agregar, consultar, actualizar y eliminar productos del inventario. Cada producto debe tener un nombre, descripción, cantidad disponible, precio unitario y categoría (como Electrónica, Ropa, Alimentos).
2. __Gestión de Stock:__ Permitir actualizar la cantidad de productos cuando se vendan o se reciban nuevas unidades.
3. __Filtrado y Búsqueda:__ Opciones de filtrado de los productos en base a las categorías y búsqueda de los productos en base a palabras dentro del nombre del producto.
4. __Generación de Reportes:__ Mostrar un resumen con el total de productos en inventario, el valor total del inventario y los productos agotados. El reporte se entregará a través de la consola del programa.
5. __Autenticación:__ Proteger el acceso con un sistema de autenticación por nombre de usuario y contraseña.



## Verificación:
Para verificar de que los requisitos previamente mencionados se estén cumpliendo, se realizarán distintas pruebas probando cada una de las funcionalidades.

Ciclo 1:
Se centró en pruebas de las funcionalidades de Login, Agregar Productos y Consultar Productos.
Se realizaron 12 pruebas generadas con IA en Greentest, de las cuales fueron exitosas 8.

![Ciclo1](./images/Greentest%20-%20Ciclo%201.png "Ciclo 1 de Pruebas")

Una vez terminadas las 12 pruebas, y con el resultado ya analizado, se procede a corregir el código para que las 4 pruebas faltantes resulten positivas.

Ciclo 2:
Se centró en pruebas de las funcionalidades de Actualizar, Eliminar y Filtrar productos y la actualización del Stock de un producto.
Se realizaron 18 pruebas generadas con IA en Greentest, de las cuales 15 resultaron exitosas.

![Ciclo2](./images/Greentest%20-%20Ciclo%202.png "Ciclo 2 de Pruebas")

Con los resultados de los tests ya en mano, se procede a corregir el código de la aplicación.

# Organización
Para el desarrollo de la tarea se realizarán push directos a la branch main del repositorio. Esto por comodidad al estar trabajando de manera solitaria.

No se crea organización en Github puesto que el repositorio fue creado antes de que el profesor indicara en clases que esto no era opción (dijo que se pusiera acá esto para no descontar).

# Flujo de Trabajo y Configuraciones
Se conectó Slack con el repositorio de Github, recibiendo mensajes cada vez que se realizaba un push al repositorio.

![Slack](./images/Github%20-%20Slack.png "Integración de Github con Slack")

# Registro de Pruebas
Las pruebas quedaron registradas en la plataforma Greentest. Desconozco si hay una manera de descargar un archivo con el detalle o de dar acceso a estas a otras personas.

__Feedback:__ Veo opciones de mejora en un pequeño tutorial de cómo usar la plataforma, puesto que tuve que ir descubriendo el cómo funciona. Ideal que al poner el mouse encima de un botón explique brevemente lo que hace. Extrañé también un menú de ayuda que me explicara para qué sirve cada botón y qué puedo hacer dentro de la aplicación. Aparte de todo esto, fue una buena experiencia, me sorprendió el que la IA entendiera bien lo que necesitaba y me diera pruebas que de verdad servían para probar funcionalidades y que además detectaron fallas en el código. Hubo un par de veces que se quedaba generando los tests de manera infinita, y al recargar la página, ya se habían generado. También me pasó que no me cargara el detalle de la suite de pruebas, una vez terminado el ciclo, que nuevamente se arregló al recargar la página.

## Supuestos realizados:
- No hay distintos roles para los usuarios.
- Los usuarios son creados por nosotros, y no por cada usuario del programa (lista de usuarios y contraseñas será incluida posteriormente).
- Las categorías de los productos son creadas por nosotros, se entregará una lista de estas posteriormente.
- El filtro solo consistirá en un filtro por la categoría de un producto. Mientras que el sistema de búsqueda será en base a palabras contenidas en los nombres de los productos.
- Cada ítem contará con un ID numérico generado automáticamente, además de un SKU específico.
- Un producto no puede tener stock negativo.
