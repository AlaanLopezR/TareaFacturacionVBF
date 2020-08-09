"""Tarea2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import menu,  producto,ventas, cliente,editarProducto,listarProducto,eliminarProducto,listarVenta
from app.views import editarCliente,listarCliente,eliminarCliente,listarDetalle


urlpatterns = [
    path('admin/', admin.site.urls),
    
    #path('ventas/', ventas, name='ventas'),
    #path('productos/', productos, name='productos'),
    #path('editarproductos/', editarproductos, name='editarproductos'),
    #path('eliminarproductos/', eliminarproductos, name='eliminarproductos'),
    #path('clientes/', clientes, name='clientes'),
    #OTROS
    #path('editarcontacto/<int:id>/', editarContacto, name='editarcontacto'),
    #path('listarcontacto/', listarContacto, name='listarcontacto'),
    #path('eliminarcontacto/<int:id>', eliminarContacto, name='eliminarcontacto'),
    path('venta/', ventas),

    path('', listarVenta, name='index'),
    path('listarventa/', listarVenta, name='listarVenta'),
    path('detalleFactura/<int:id>/', listarDetalle, name='detalleFactura'),
    
    path('cliente/', cliente, name='cliente'),
    path('editarcliente/<int:id>/', editarCliente, name='editarCliente'),
    path('listarcliente/', listarCliente, name='listarCliente'),
    path('eliminarcliente/<int:id>', eliminarCliente, name='eliminarCliente'),


    path('producto/', producto, name='producto'),
    path('editarproducto/<int:id>/', editarProducto, name='editarProducto'),
    path('listarproducto/', listarProducto, name='listarProducto'),
    path('eliminarproducto/<int:id>', eliminarProducto, name='eliminarProducto'),
]
