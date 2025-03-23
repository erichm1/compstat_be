from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CrimeIncidentViewSet, CriminalViewSet, CriminalOffenseViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'crimes', CrimeIncidentViewSet)
router.register(r'criminals', CriminalViewSet)
router.register(r'offenses', CriminalOffenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Append static URLs to urlpatterns for static files like images, CSS, and JS in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Append media URLs for uploaded files (optional, based on your project needs)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)