# Proyecto de Automatización Web - SauceDemo


## Propósito
Automatizar pruebas funcionales de la aplicación web SauceDemo para validar el proceso de inicio de sesión, la visualización del catálogo de productos y la gestión del carrito de compras mediante Selenium WebDriver y Pytest.
Repositorio del proyecto:
https://github.com/alanliberman1/automatizacion-curso
---


## Tecnologías Utilizadas
- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- Google Chrome
---


## Instalación de Dependencias

Instalar las dependencias necesarias ejecutando:
```bash
pip install selenium
pip install pytest
pip install pytest-html
```
---


## Ejecución de las Pruebas

Ejecutar todas las pruebas:
```bash
pytest
```

Ejecutar las pruebas mostrando información detallada y los mensajes impresos por consola:
```bash
pytest -v -s
```
---
## Casos de Prueba Implementados


### Login Exitoso
Validaciones realizadas:
- Ingreso con credenciales válidas.
- Verificación de URL posterior al login.
- Validación del logo de la aplicación.
- Validación del título de la página.


### Validaciones del Catálogo
Validaciones realizadas:
- Verificación del título de la página.
- Validación de existencia de productos.
- Validación de cantidad de productos mostrados.
- Verificación del nombre y precio del primer producto.
- Verificación de los nombres de todos los productos del catálogo.
- Validación de elementos visibles como menú hamburguesa y filtro de productos.


### Agregar Producto al Carrito
Validaciones realizadas:
- Verificación de carrito vacío.
- Agregado de producto al carrito.
- Validación del incremento del contador del carrito.
- Acceso a la página del carrito.
- Verificación del título de la página.
- Validación del producto agregado.
---


## Reportes
El proyecto se encuentra configurado para generar automáticamente un reporte HTML luego de cada ejecución.
Ubicación del reporte:
```text
reports/reporte.html
```
El reporte contiene:
- Resultado de las pruebas ejecutadas.
- Casos aprobados y fallidos.
- Tiempo de ejecución.
- Detalle de cada prueba.