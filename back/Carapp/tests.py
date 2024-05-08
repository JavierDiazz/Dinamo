from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
from .views import *
from rest_framework import serializers
from .serializers import *
from .routers import *
from rest_framework.test import APITestCase
from rest_framework import status

# Create your tests here.
class RegistroUsuariosTest(APITestCase):
    def test_registro_usuario_exitoso(self):
        data = {
            'username': 'usuario_prueba',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'phone': '123456789',
            'email': 'usuario@prueba.com',
            'password': 'contraseña123',
            'idSede': 1
        }
        response = self.client.post('/carapp/user/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='usuario_prueba').exists())

class RegistroAutosTest(APITestCase):
    def test_registro_auto_exitoso(self):
        data = {
            'idAuto': 'ABC123',
            'modelo': 'Modelo de prueba',
            'color': 'Rojo',
            'precio': 10000,
            'año': 2022,
            'descripcion': 'Descripción del auto',
            'foto': 'url_de_la_foto',
            'idSede': 1
        }
        response = self.client.post('/carapp/autos/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Auto.objects.filter(idAuto='ABC123').exists())

class BusquedaTest(APITestCase):
    def setUp(self):
        self.auto1 = Auto.objects.create(idAuto='ABC123', modelo='Modelo de prueba 1', color='Rojo', precio=10000, año=2022, descripcion='Descripción del auto', foto='url_de_la_foto')
        self.auto2 = Auto.objects.create(idAuto='XYZ456', modelo='Modelo de prueba 2', color='Azul', precio=15000, año=2023, descripcion='Otra descripción', foto='url_de_la_foto')
        
    def test_busqueda_exitosa(self):
        data = {
            'idAuto': 'ABC123',
            'modelo': 'Modelo de prueba 1',
            'año': 2022
        }
        response = self.client.get('/carapp/autos/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

class ValidacionCamposTest(APITestCase):
    def setUp(self):
        self.username = 'usuario_prueba'
        self.password = 'contraseña123'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        
    def test_creacion_usuario_campos_obligatorios(self):
        # Intenta crear un usuario sin proporcionar todos los campos obligatorios
        data = {
            'username': 'nuevo_usuario',
            # Falta el campo obligatorio 'password'
        }
        response = self.client.post('/carapp/user/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Verifica que el mensaje de error esperado esté presente en la respuesta
        self.assertEqual(response.data['password'][0], 'This field is required.')
    
    def test_creacion_auto_campos_obligatorios(self):
        # Intenta crear un auto sin proporcionar todos los campos obligatorios
        data = {
            'idAuto': 'ABC123',
            # Falta el campo obligatorio 'precio'
        }
        response = self.client.post('/carapp/autos/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Verifica que el mensaje de error esperado esté presente en la respuesta
        self.assertEqual(response.data['precio'][0], 'This field is required.')