from django.contrib import admin
from Carapp.models import *

class rol_admin(admin.ModelAdmin):
    list_display = ('id', 'idRol')
    list_filter = ('id', 'idRol')

class rol_user_admin(admin.ModelAdmin):
    list_display = ('idRol', 'idUsuario')

class sede_admin(admin.ModelAdmin):
    list_display = ('id', 'idSede')
    list_filter = ('id', 'idSede')
    search_fields = ('id', 'idSede')

class sede_user_admin(admin.ModelAdmin):
    list_display = ('idSede', 'idUsuario')

class auto_admin(admin.ModelAdmin):
    list_display = ('id', 'idAuto', 'modelo', 'color', 'precio', 'año', 'descripcion', 'foto')
    list_filter = ('idAuto', 'modelo', 'color', 'año')
    search_fields = ('idAuto', 'modelo', 'color', 'año')

class sede_auto_admin(admin.ModelAdmin):
    list_display = ('idSede', 'idAuto')


admin.site.register(Rol,rol_admin)
admin.site.register(UsuarioRol,rol_user_admin)
admin.site.register(Sede,sede_admin)
admin.site.register(UsuarioSede,sede_user_admin)
admin.site.register(Auto,auto_admin)
admin.site.register(AutoSede,sede_auto_admin)

