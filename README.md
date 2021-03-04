# Módulo Ventas

Se trata de un módulo de ventas muy sencillo creado desde cero.

## Clases
 
Tiene tres clases:
- Product
- Consumer
- Sale

Cada producto tiene: una imagen, un nombre, una descripción, un stock y un precio. El stock por defecto es 1 y ni este ni el precio pueden tener valores nagativos.

Los consumidores son heredados del modelo res.partner, a los que se les añade una fecha de nacimiento y un país de procedencia.

Para crear una venta necesitamos un consumidor, un producto, la fecha de venta, que por defecto es la del día en el que se crea la venta; un descuento que se aplicará a la compra y la cantidad que queremos de dicho producto.

Tanto el descuento como la cantidad deben ser números positivos y, además, la cantidad que se pide no debe ser superior al stock que existe actualmente del producto en cuestión.

## Vistas

Todos los modelos tienen vistas de formulario y de árbol o lista.

En las vistas de lista:

- Para los productos se muestran: el nombre, el stock y el precio.
- Para los consumidores: el nombre y el número de teléfono, al que se puede acceder ya que es uno de los atributos del modelo del que se hereda.
- Para las ventas: el nombre del consumidor, el del producto, la fecha de compra, la cantidad comprada y el precio total

Además de la vista de tipo lista que tiene el modelo de ventas, este también tiene una vista tipo kanban, en el que se muestran: una foto del producto, el nombre del consumidor, la fecha de compra, la cantidad y el precio total.
