from django import forms
from .models import Producto, Cliente, Factura, DetalleFactura


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('descripcion', 'precio', 'stock', 'iva')
        label = {'descripcion': 'Descripción', 'precio': 'Precio', 'stock': 'Stock', 'iva': 'IVA'}

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('ruc', 'nombre', 'direccion', 'producto')
        label = {'ruc': 'RUC', 'nombre': 'Nombre', 'direccion': 'Dirección', 'producto': 'Producto'}

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ('cliente', 'fecha', 'total')
        label = {'cliente': 'Cliente', 'fecha': 'Fecha', 'total': 'Total'}

class DetalleForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = ('factura', 'producto', 'cantidad', 'precio', 'subtotal')
        label = {'factura': 'Factura', 'producto': 'Producto', 'cantidad': 'Cantidad', 'precio': 'Precio', 'subtotal': 'Subtotal'}

