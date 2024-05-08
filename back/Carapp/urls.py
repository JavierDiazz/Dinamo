from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

urlpatterns = [
    # URLs de tu aplicación...
    path('', include(router.urls)),
]