from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

#Modelo de la tabla Rol
class Rol(models.Model):
    idRol = models.CharField(max_length=50, unique=True)
    
    class Meta:
        db_table = 'Rol' 
    
#Modelo de la tabla UsuarioRol
class UsuarioRol(models.Model):
    idUsuario=models.ForeignKey(User,on_delete=models.CASCADE,default=0,related_name='idUsuario_UsuarioRol')
    idRol=models.ForeignKey(Rol,on_delete=models.CASCADE,default=0,related_name='idRol_UsuarioRol')
    
    class Meta:
        db_table = 'UsuarioRol'
        
#Modelo de la tabla Sede
class Sede(models.Model):
    idSede = models.CharField(max_length=50, unique=True)
    
    class Meta:
        db_table = 'Sede' 

#Modelo de la tabla UsuarioSede
class UsuarioSede(models.Model):
    idUsuario=models.ForeignKey(User,on_delete=models.CASCADE,default=0,related_name='idUsuario_UsuarioSede')
    idSede=models.ForeignKey(Sede,on_delete=models.CASCADE,default=0,related_name='idSede_UsuarioSede')
    
    class Meta:
        db_table = 'UsuarioSede'

#Modelo de la tabla Auto
class Auto(models.Model):
    idAuto = models.CharField(max_length=50, default=None)
    modelo = models.CharField(max_length=50,default=None)
    color = models.CharField(max_length=50,default=None)
    precio = models.BigIntegerField()
    año = models.IntegerField()
    descripcion = models.CharField(max_length=150,default=None)
    foto = models.CharField(max_length=50,default=None)
    
    class Meta:
        db_table = 'Auto'

#Modelo de la tabla AutoSede
class AutoSede(models.Model):
    idAuto=models.ForeignKey(Auto,on_delete=models.CASCADE,default=0,related_name='idAuto_AutoSede')
    idSede=models.ForeignKey(Sede,on_delete=models.CASCADE,default=0,related_name='idSede_AutoSede')
    
    class Meta:
        db_table = 'AutoSede'