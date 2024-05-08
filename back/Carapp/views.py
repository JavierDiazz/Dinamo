from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from rest_framework import serializers
from rest_framework import viewsets
from django.core.serializers import serialize
from rest_framework.permissions import IsAuthenticated
from .serializers import *

# Create your views here.

"""
    Viewsets del modelo de usuario.

    Esta vista permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar)
    en el modelo de usuarios.

    Permisos:
    - El usuario debe estar autenticado para acceder a esta vista.

    Serializer:
    - Se utiliza 'user_serializer' para serializar los datos del modelo.

    Atributos:
    - serializer_class: Clase del serializador utilizado.
    - permission_classes: Clases de permisos aplicadas a la vista.
    - queryset: Conjunto de objetos del modelo 'User'.

    Métodos HTTP admitidos:
    - GET: Obtiene una lista de usuarios.
    - POST: Crea un nuevo usuario.
    - PUT: Actualiza un usuario existente.
    - DELETE: Elimina un usuario existente.

    Gestión de solicutudes HTTP VIEWSETS:
    list: Maneja las solicitudes GET para obtener una lista de recursos.
    create: Maneja las solicitudes POST para crear un nuevo recurso.
    retrieve: Maneja las solicitudes GET para obtener un recurso específico por su clave primaria.
    update: Maneja las solicitudes PUT para actualizar un recurso específico por su clave primaria.
    partial_update: Maneja las solicitudes PATCH para realizar una actualización parcial de un recurso específico por su clave primaria.
    destroy: Maneja las solicitudes DELETE para eliminar un recurso específico por su clave primaria.
"""


class sede_viewsets (viewsets.ModelViewSet):
    serializer_class = sede_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = sede_serializer.Meta.model.objects.all()

class usuario_sede_viewsets (viewsets.ModelViewSet):
    serializer_class = usuario_sede_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = usuario_sede_serializer.Meta.model.objects.all()

class rol_viewsets (viewsets.ModelViewSet):
    serializer_class = rol_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = rol_serializer.Meta.model.objects.all()

class usuario_rol_viewsets (viewsets.ModelViewSet):
    serializer_class = usuario_rol_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = usuario_rol_serializer.Meta.model.objects.all()

class user_viewsets (viewsets.ModelViewSet):
    serializer_class = user_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = user_serializer.Meta.model.objects.all()

class auto_viewsets (viewsets.ModelViewSet):
    serializer_class = auto_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = auto_serializer.Meta.model.objects.all()

class auto_sede_viewsets (viewsets.ModelViewSet):
    serializer_class = auto_sede_serializer
    #permission_classes = (IsAuthenticated,)
    queryset = auto_sede_serializer.Meta.model.objects.all()