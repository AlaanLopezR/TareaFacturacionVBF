from django.contrib import admin
from .models import Factura, Cliente, Producto, DetalleFactura

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display=('ruc','nombre','direccion')
    ordering=('nombre',)
    search_fields=('ruc','nombre')
    list_filter=('nombre',)

class ProductoAdmin(admin.ModelAdmin):
    list_display=('descripcion','precio','stock','iva')
    ordering=('descripcion',)
    list_filter=('descripcion',)

class FacturaAdmin(admin.ModelAdmin):
    list_display=('cliente','fecha','total')
    ordering=('fecha',)
    list_filter=('cliente',)

class DetalleAdmin(admin.ModelAdmin):
    list_display=('factura','producto','cantidad','precio','subtotal')
    ordering=('factura',)
    list_filter=('factura',)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(DetalleFactura, DetalleAdmin)