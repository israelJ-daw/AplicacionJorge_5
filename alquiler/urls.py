from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    # URLs para Usuario
    path('usuarios/', views.usuario_lista, name='usuario_lista'),
    path('usuarios/crear/', views.usuario_crear, name='usuario_crear'),
    path('usuarios/<int:usuario_id>/editar/', views.usuario_actualizar, name='usuario_actualizar'),
    path('usuarios/<int:usuario_id>/eliminar/', views.usuario_delete, name='usuario_delete'),

    # URLs para Perfil
    path('perfiles/', views.perfil_lista, name='perfil_lista'),
    path('perfiles/crear/', views.perfil_crear, name='perfil_crear'),
    path('perfiles/<int:perfil_id>/editar/', views.perfil_actualizar, name='perfil_actualizar'),
    path('perfiles/<int:perfil_id>/eliminar/', views.perfil_delete, name='perfil_delete'),

    # URLs para Categoria
    path('categorias/', views.categoria_lista, name='categoria_lista'),
    path('categorias/crear/', views.categoria_crear, name='categoria_crear'),
    path('categorias/<int:categoria_id>/editar/', views.categoria_actualizar, name='categoria_actualizar'),
    path('categorias/<categoria_id>/eliminar/', views.categoria_delete, name='categoria_delete'),

    # URLs para ServicioExtra
    path('serviciosextra/', views.servicioextra_lista, name='servicioextra_lista'),
    path('serviciosextra/crear/', views.servicioextra_crear, name='servicioextra_crear'),
    path('serviciosextra/<int:servicio_extra_id>/editar/', views.servicioextra_actualizar, name='servicioextra_actualizar'),
    path('serviciosextra/<int:servicio_extra_id>/eliminar/', views.servicioextra_delete, name='servicioextra_delete'),

    # URLs para Propiedad
    path('propiedades/', views.propiedad_lista, name='propiedad_lista'),
    path('propiedades/crear/', views.propiedad_crear, name='propiedad_crear'),
    path('propiedades/<int:propiedad_id>/editar/', views.propiedad_actualizar, name='propiedad_actualizar'),
    path('propiedades/<int:propiedad_id>/eliminar/', views.propiedad_delete, name='propiedad_delete'),

    # URLs para Prioridad
    path('prioridades/', views.prioridad_lista, name='prioridad_lista'),
    path('prioridades/crear/', views.prioridad_crear, name='prioridad_crear'),
    path('prioridades/<int:prioridad_id>/editar/', views.prioridad_actualizar, name='prioridad_actualizar'),
    path('prioridades/<int:prioridad_id>/eliminar/', views.prioridad_delete, name='prioridad_delete'),

    path('usuarios/<str:email>/', views.usuario_detalle, name='usuario_detalle'),  # OneToOne
    path('propiedades/', views.lista_propiedades, name='lista_propiedades'),  # ManyToMany
    path('categorias/<int:id>/', views.detalle_categoria, name='detalle_categoria'),  # QuerySet con parámetros
    path('propiedad/reservas/<int:propiedad_id>/', views.reservas_propiedad, name='reservas_propiedad'),  # Filtro ManyToOne
    path('comentarios/propiedad/<int:propiedad_id>/', views.comentarios_propiedad, name='comentarios_propiedad'),  # Reverse
    path('reservas/filtro/', views.filtrar_reservas, name='filtrar_reservas'),  # Filtros con AND y OR
    path('categorias/none/', views.categorias_sin_propiedades, name='categorias_sin_propiedades'),  # None intermedio
    path('propiedades/precios/', views.propiedad_precio_agregado, name='propiedad_precio_agregado'),  # Aggregate
    path('usuarios/recientes/', views.usuarios_recientes, name='usuarios_recientes'),# OrderBy y limit
    path('error/404/', views.error_404, name='error_404'),  # Error personalizado
    path('error/404/', views.error_404, name='error_404'),  # Error personalizado
    path('error/404/', views.error_404, name='error_404'),  # Error personalizado
    path('error/404/', views.error_404, name='error_404'),  # Error personalizado

]