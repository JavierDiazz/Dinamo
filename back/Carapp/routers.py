from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
"""
    Endpoints
"""
router.register(r'user', user_viewsets,basename='user')
router.register(r'sedes', sede_viewsets,basename='sedes')
router.register(r'roles', rol_viewsets,basename='roles')
router.register(r'user_sede', usuario_sede_viewsets,basename='user_sede')
router.register(r'user_rol', usuario_rol_viewsets,basename='user_rol')
router.register(r'autos', auto_viewsets,basename='autos')
router.register(r'auto_sede', auto_sede_viewsets,basename='auto_sede')

urlpatterns = router.urls