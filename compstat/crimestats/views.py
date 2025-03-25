from rest_framework import viewsets
from .models import CrimeStat, CrimeStatSummary, CrimeTrend, CrimeHeatmap
from .serializers import CrimeStatSerializer, CrimeStatSummarySerializer, CrimeTrendSerializer, CrimeHeatmapSerializer

class CrimeStatViewSet(viewsets.ModelViewSet):
    queryset = CrimeStat.objects.all()
    serializer_class = CrimeStatSerializer

class CrimeStatSummaryViewSet(viewsets.ModelViewSet):
    queryset = CrimeStatSummary.objects.all()
    serializer_class = CrimeStatSummarySerializer

class CrimeTrendViewSet(viewsets.ModelViewSet):
    queryset = CrimeTrend.objects.all()
    serializer_class = CrimeTrendSerializer

class CrimeHeatmapViewSet(viewsets.ModelViewSet):
    queryset = CrimeHeatmap.objects.all()
    serializer_class = CrimeHeatmapSerializer