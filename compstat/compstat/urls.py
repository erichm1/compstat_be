from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.views import CrimeIncidentViewSet, CriminalViewSet, CriminalOffenseViewSet
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'crimes', CrimeIncidentViewSet)
router.register(r'criminals', CriminalViewSet)
router.register(r'offenses', CriminalOffenseViewSet)

# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="CompStat API",
        default_version='v1',
        description="Documentação da API do CompStat",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@compstat.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    # URLs para a documentação Swagger e Redoc
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


# Append static URLs to urlpatterns for static files like images, CSS, and JS in development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Append media URLs for uploaded files (optional, based on your project needs)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)