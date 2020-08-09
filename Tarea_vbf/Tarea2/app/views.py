from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductoForm, ClienteForm, FacturaForm, DetalleForm
from .models import Cliente, Producto, Factura, DetalleFactura


# Create your views here.
def menu(request):
    opciones = {'Ventas': 'Ventas',
                'Producto': 'Producto',
                'Cliente': 'Cliente',
                'Administracion': 'Administracion'}
    return render(request, 'listar_ventas.html', opciones)


def ventas(request):
    opciones = {'Ventas': 'Ventas',
                'Producto': 'Productos',
                'Cliente': 'Clientes',
                'Administracion': 'Administracion'}
    return render(request, 'ventas.html', opciones)




def contacto(request):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Contacto del Blog', 'Acerca': 'Acerca del Blog', 'accion': 'Crear'}
    # return HttpResponse('Contacto')
    if request.method == 'POST':
        # pass
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarcontacto')
    else:
        form = ContactoForm()
        opciones['form'] = form

    return render(request, 'contacto.html', opciones)


def editarContacto(request, id):
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Contacto del Blog', 'Acerca': 'Acerca del Blog', 'accion': 'Actualizar'}
    contacto = Contacto.objects.get(id=id)
    if request.method == 'GET':
        form = ContactoForm(instance=contacto)
        opciones['form'] = form
    else:
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('listarcontacto')

    return render(request, 'contacto.html', opciones)


def listarContacto(request):
    contacto = Contacto.objects.all()
    opciones = {'Menu': 'Menu Principal',
                'Contacto': 'Contacto del Blog', 'Acerca': 'Acerca del Blog', 'contactos': contacto}
    return render(request, 'listar_contacto.html', opciones)



def eliminarContacto(request, id):
    contacto = Contacto.objects.get(id=id)
    if request.method == 'POST':
        contacto.delete()
        return redirect('listarcontacto')
    return render(request, 'eliminar_contacto.html', {'Contacto': contacto})


#################################################################
################################PRODUCTO#########################
#################################################################
def listarProducto(request):
    productos = Producto.objects.all()
    opciones = {'Ventas': 'Ventas',
                'Producto': 'Productos',
                'Cliente': 'Clientes',
                'Administracion': 'Administracion',
                'productos':productos}
    return render(request, 'listar_productos.html', opciones)

def producto(request):
    opciones = {'Ventas': 'Ventas',
                'Producto': 'Productos',
                'Cliente': 'Clientes',
                'Administracion': 'Administracion',
                'accion': 'Crear'}
    if request.method == 'POST':
        # pass
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarProducto')
    else:
        form = ProductoForm()
        opciones['form'] = form
    return render(request, 'producto.html', opciones)

def editarProducto(request, id):
    opciones = {'Ventas': 'Ventas',
                'Producto': 'Productos',
                'Cliente': 'Clientes',
                'Administracion': 'Administracion',
                'accion': 'Modificar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listarProducto')
    return render(request, 'producto.html', opciones)

def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listarProducto')
    return render(request, 'eliminar_producto.html', {'Producto': producto})


#########################################################################
#################################CLIENTES################################
#########################################################################
def listarCliente(request):
    clientes = Cliente.objects.all()
    opciones = {'Ventas': 'Ventas',
                'Producto': 'Productos', 
                'Cliente': 'Clientes',
                'Administracion': 'Administracion',
                'clientes': clientes}
    return render(request, 'listar_clientes.html', opciones)

def cliente(request):
    opciones = {'Ventas': 'Ventas',
                'Producto': 'Productos', 
                'Cliente': 'Clientes',
                'Administracion': 'Administracion',
                'accion': 'Crear'}
    if request.method == 'POST':
        # pass
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarCliente')
    else:
        form = ClienteForm()
        opciones['form'] = form
    return render(request, 'cliente.html', opciones)

def editarCliente(request, id):
    opciones = {'Ventas': 'Ventas',
                'Producto': 'Productos', 
                'Cliente': 'Clientes',
                'Administracion': 'Administracion',
                'accion': 'Modificar'}
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = ClienteForm(instance=cliente)
        opciones['form'] = form
    else:
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('listarCliente')
    return render(request, 'cliente.html', opciones)

def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listarCliente')
    return render(request, 'eliminar_cliente.html', {'Cliente': cliente})


#########################################################################
#################################FACTURA################################
#########################################################################
def listarVenta(request):
    facturas = Factura.objects.all()    
    opciones = {'Ventas': 'Ventas',
                'Producto': 'Productos',
                'Cliente': 'Clientes',
                'Administracion': 'Administracion',
                'facturas': facturas}
    return render(request, 'listar_ventas.html', opciones)

def listarDetalle(request, id):
    detalles = DetalleFactura.objects.filter(factura=id)
    opciones = {'DetalleFactura': 'Detalle de Factura',
                'Ventas': 'Ventas',
                'Producto': 'Productos',
                'Cliente': 'Clientes',
                'Administracion': 'Administracion',
                'detalles': detalles}
    return render(request, 'listar_detalle.html', opciones)
