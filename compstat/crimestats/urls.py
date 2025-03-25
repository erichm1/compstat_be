from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CrimeStatViewSet, CrimeStatSummaryViewSet, CrimeTrendViewSet, CrimeHeatmapViewSet

router = DefaultRouter()
router.register(r'crime-stats', CrimeStatViewSet)
router.register(r'crime-stat-summaries', CrimeStatSummaryViewSet)
router.register(r'crime-trends', CrimeTrendViewSet)
router.register(r'crime-heatmaps', CrimeHeatmapViewSet)

urlpatterns = [
    path('', include(router.urls)),
]