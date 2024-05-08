from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class user_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = User
		fields = '__all__'
		

class rol_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Rol
		fields = '__all__'
		
class usuario_rol_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = UsuarioRol
		fields = '__all__'
		
class sede_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Sede
		fields = '__all__'
		
class usuario_sede_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = UsuarioSede
		fields = '__all__'
		
class auto_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = Auto
		fields = '__all__'
		
class auto_sede_serializer(serializers.ModelSerializer):

	# create a meta class
	class Meta:
		model = AutoSede
		fields = '__all__'