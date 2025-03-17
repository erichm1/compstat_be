from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CrimeIncidentViewSet

router = DefaultRouter()
router.register(r'crimes', CrimeIncidentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]