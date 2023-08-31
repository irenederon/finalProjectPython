from django.db import models

# Create your models here.


class Proveedor(models.Model):
	nombre_proveedor = models.TextField(null=False)
	telefono_proveedor = models.TextField(null=False)
	direccion_proveedor = models.TextField(null=False)
	cif_proveedor = models.TextField(null=False)
	facturacion_proveedor = models.FloatField(null=False)
	def __str__(self):
		return self.nombre_proveedor


class Producto(models.Model):
	referencia_producto = models.TextField(null=False)
	descripcion_producto = models.TextField(null=False)
	almacen_producto = models.TextField(null=False)
	precio_producto = models.FloatField(null=False)
	stockMax_producto = models.IntegerField(null=False)
	stockActual_producto = models.IntegerField(null=False)
	iva_producto = models.IntegerField(null=False)
	descuento_producto = models.IntegerField(default=0)
	proveedor_producto = models.ForeignKey(Proveedor, on_delete=models.CASCADE, )
	def __str__(self):
		return self.descripcion_producto

class Cliente(models.Model):
	nombre_cliente = models.TextField(null=False)
	telefono_cliente = models.TextField(null=False)
	direccion_cliente = models.TextField(null=False)
	cif_cliente = models.TextField(null=False)
	gasto_cliente = models.FloatField(null=False, default=0)
	def __str__(self):
		return self.nombre_cliente


class Compra(models.Model):
	producto_compra = models.ForeignKey(Producto, on_delete=models.CASCADE, )
	cantidad_compra = models.IntegerField(null=False)
	precio_compra = models.FloatField(null=False)
	def __str__(self):
		return "Se han comprado ", self.cantidad_compra , \
			   " unidades del producto ",self.producto_compra.descripcion_producto

class Venta(models.Model):
	producto_venta = models.ForeignKey(Producto, on_delete=models.CASCADE, )
	cliente_venta = models.ForeignKey(Cliente, on_delete=models.CASCADE, )
	cantidad_venta = models.IntegerField(null=False)
	precio_venta = models.FloatField(null=False)
	def __str__(self):
		return "Se han vendido ", self.cantidad_venta, \
			   " unidades del producto ", self.producto_venta.descripcion_producto