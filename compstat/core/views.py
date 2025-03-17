from django.shortcuts import render
from rest_framework import viewsets
from .models import CrimeIncident
from .serializers import CrimeIncidentSerializer

class CrimeIncidentViewSet(viewsets.ModelViewSet):
    queryset = CrimeIncident.objects.all().order_by('-date_time')
    serializer_class = CrimeIncidentSerializer