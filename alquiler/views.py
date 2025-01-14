# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg  
from django.db.models import Q 
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, "index.html")



# Obtiene detalles de un usuario por su email.
def usuario_detalle(request, email):
    usuario = get_object_or_404(Usuario.objects.select_related('perfil'), email=email)
    return render(request, 'usuario_detalle.html', {'usuario': usuario})


# Muestra todas las propiedades con sus categorías y servicios extra.
def lista_propiedades(request):
    propiedades = Propiedad.objects.prefetch_related('categoria', 'servicios_extra')
    return render(request, 'lista_propiedades.html', {'propiedades': propiedades})


# Detalle de una categoría específica.
def detalle_categoria(request, id):
    categoria = Categoria.objects.prefetch_related('propiedades').get(id=id)
    return render(request, 'detalle_categoria.html', {'categoria': categoria})


# Lista las reservas asociadas a una propiedad específica.
def reservas_propiedad(request, propiedad_id):
    reservas = Reserva.objects.filter(propiedad_id=propiedad_id).select_related('perfil', 'pago')
    return render(request, 'reservas_propiedad.html', {'reservas': reservas})


# Muestra los comentarios de una propiedad.
def comentarios_propiedad(request, propiedad_id):
    propiedad = Propiedad.objects.prefetch_related('comentarios').get(id=propiedad_id)
    return render(request, 'comentarios_propiedad.html', {'propiedad': propiedad})


# Filtra reservas por estado y rango de fechas.
def filtrar_reservas(request):
    reservas = Reserva.objects.filter(
        Q(estado="Whole war mother.") & Q(total__gte=0.446948437705188) | Q(estado="Event cover none.")
    )
    return render(request, 'filtrar_reservas.html', {'reservas': reservas})



# Categorías sin propiedades asignadas.
def categorias_sin_propiedades(request):
    categorias = Categoria.objects.filter(propiedades=None)
    return render(request, 'categorias_sin_propiedades.html', {'categorias': categorias})


# Calcula el precio promedio de las propiedades.
def propiedad_precio_agregado(request):
    precio_promedio = Propiedad.objects.aggregate(Avg('precio_por_noche'))
    return render(request, 'propiedad_precio_agregado.html', {'precio_promedio': precio_promedio})

#esta view no me sale y no encuentro el error 

def usuarios_recientes(request):
    # Obtener los 10 usuarios más recientes ordenados por fecha_registro
    usuarios = Usuario.objects.order_by('-fecha_registro')[:10]
    # Pasar los usuarios a la plantilla
    return render(request, 'usuarios_recientes.html', {'usuarios': usuarios})


# Muestra una página personalizada de error 404.
def error_404(request, exception=None):
    return render(request, 'errores/error_404.html', None, None, 400)


# Muestra una página personalizada de error 400.
def error_400(request, exception=None):
    return render(request, 'errores/error_400.html', None, None, 400)


# Muestra una página personalizada de error 403.
def error_403(request, exception=None):
    return render(request, 'errores/error_403.html', None, None, 400)


# Muestra una página personalizada de error 500.
def error_500(request, exception=None):
    return render(request, 'errores/error_500.html', None, None, 400)


#Formularios-------------------------------------

# CRUD para Usuario
def usuario_lista(request):
    usuarios = Usuario.objects.all()
    return render(request, 'Usuario/usuario_lista.html', {'usuarios': usuarios})

def usuario_crear(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_lista')
    else:  
        form = UsuarioForm()

    return render(request, 'Usuario/usuario_crear.html', {'form': form})

def usuario_actualizar(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'Usuario/usuario_actualizar.html', {'form': form})


def usuario_delete(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST': 
        usuario.delete()  
        return redirect('usuario_lista') 

    return render(request, 'Usuario/usuario_eliminar.html', {'usuario': usuario})



# CRUD para Perfil
def perfil_lista(request):
    perfiles = Perfil.objects.all()
    return render(request, 'Perfil/perfil_lista.html', {'perfiles': perfiles})

#este view, no se porque me funciona, no me da ningun error, pero no consigo que me guarde el perfil en la base de datos. No encuentro solucion
def perfil_crear(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        
        if form.is_valid():
            perfil = form.save(commit=False)
            
            # Aqui se asigna el usuario 
            usuario_predeterminado = Usuario.objects.first() 

            # si el usuario ya tiene un perfil
            if Perfil.objects.filter(usuario=usuario_predeterminado).exists():
               
                return redirect('perfil_lista')  

            # Asignar el usuario al perfil antes de guardarlo
            perfil.usuario = usuario_predeterminado

            form.save()

            return redirect('perfil_lista')  

    else:
        form = PerfilForm()

    return render(request, 'Perfil/perfil_crear.html', {'form': form})



def perfil_actualizar(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil_lista')

    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'Perfil/perfil_actualizar.html', {'form': form})

def perfil_delete(request, perfil_id):
    perfil = get_object_or_404(Perfil, id=perfil_id)
    
    if request.method == 'POST':  
        perfil.delete() 
        return redirect('perfil_lista')  

    return render(request, 'Perfil/perfil_eliminar.html', {'perfil': perfil})

# CRUD para Categoria
def categoria_lista(request):
    categorias = Categoria.objects.all()
    return render(request, 'Categoria/categoria_lista.html', {'categorias': categorias})

def categoria_crear(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_lista')

    else:
        form = CategoriaForm()
    return render(request, 'Categoria/categoria_crear.html', {'form': form})

def categoria_actualizar(request, categoria_id):
    categoria= get_object_or_404(Categoria, id=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_lista')

    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'Categoria/categoria_actualizar.html', {'form': form})


def categoria_delete(request, categoria_id):
    categorias = get_object_or_404(Categoria, id=categoria_id)
    
    if request.method == 'POST':  
        categorias.delete() 
        return redirect('categoria_lista')  

    return render(request, 'Categoria/categoria_eliminar.html', {'categorias': categorias})

# CRUD para ServicioExtra
def servicioextra_lista(request):
    servicios = ServicioExtra.objects.all()
    return render(request, 'Servicio_extra/servicio_lista.html', {'servicios': servicios})

def servicioextra_crear(request):
    if request.method == 'POST':
        form = ServicioExtraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicioextra_lista')  

    else:
        form = ServicioExtraForm()
    return render(request, 'Servicio_extra/servicio_crear.html', {'form': form})

def servicioextra_actualizar(request, servicio_extra_id):
    categoria= get_object_or_404(ServicioExtra, id=servicio_extra_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid(): 
            form.save()
            return redirect('servicioextra_lista')

    else:
        form = ServicioExtraForm(instance=ServicioExtra)
    return render(request, 'Servicio_extra/servicio_actualizar.html', {'form': form})

def servicioextra_delete(request, servicio_extra_id):
    servicio = get_object_or_404(ServicioExtra, id=servicio_extra_id)
    if request.method == 'POST':
        servicio.delete()
        return redirect('servicioextra_lista')  

    return render(request, 'Servicio_extra/servicio_eliminar.html', {'object': servicio})

# CRUD para Propiedad
def propiedad_lista(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'Propiedad/propiedad_lista.html', {'propiedades': propiedades})

def propiedad_crear(request):
    if request.method == 'POST':
        form = PropiedadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('propiedad_lista')  

    else:
        form = PropiedadForm()
    return render(request, 'Propiedad/propiedad_crear.html', {'form': form})

def propiedad_actualizar(request, propiedad_id):
    propiedad = get_object_or_404(Propiedad, id=propiedad_id)
    if request.method == 'POST':
        form = PropiedadForm(request.POST, instance=propiedad)
        if form.is_valid():
            form.save()
            return redirect('propiedad_lista')  

    else:
        form = PropiedadForm(instance=propiedad)
    return render(request, 'Propiedad/propiedad_actualizar.html', {'form': form})

def propiedad_delete(request, propiedad_id):
    servicio = get_object_or_404(Propiedad, id=propiedad_id)
    if request.method == 'POST':
        servicio.delete()
        return redirect('propiedad_lista')  

    return render(request, 'Propiedad/propiedad_eliminar.html', {'object': servicio})

# CRUD para Prioridad
def prioridad_lista(request):
    prioridades = Prioridad.objects.all()
    return render(request, 'Prioridad/prioridad_lista.html', {'prioridades': prioridades})

def prioridad_crear(request):
    if request.method == 'POST':
        form = PrioridadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prioridad_lista')  

    else:
        form = PrioridadForm()
    return render(request, 'Prioridad/prioridad_crear.html', {'form': form})

def prioridad_actualizar(request, prioridad_id):
    prioridad = get_object_or_404(Prioridad, id=prioridad_id)
    if request.method == 'POST':
        form = PrioridadForm(request.POST, instance=prioridad)
        if form.is_valid():
            form.save()
            return redirect('prioridad_lista')

    else:
        form = PrioridadForm(instance=prioridad)
    return render(request, 'Prioridad/prioridad_actualizar.html', {'form': form})

def prioridad_delete(request, prioridad_id):
    prioridad = get_object_or_404(Prioridad, id=prioridad_id)
    
    if request.method == 'POST':
        prioridad.delete()
        return redirect('prioridad_lista')  

    return render(request, 'Prioridad/prioridad_eliminar.html', {'prioridad': prioridad})

