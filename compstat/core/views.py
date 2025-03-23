from django.shortcuts import render
from rest_framework import viewsets
from .models import CrimeIncident, Criminal, CriminalOffense
from .serializers import CrimeIncidentSerializer, CriminalSerializer, CriminalOffenseSerializer

class CrimeIncidentViewSet(viewsets.ModelViewSet):
    queryset = CrimeIncident.objects.all().order_by('-date_time')
    serializer_class = CrimeIncidentSerializer

class CriminalViewSet(viewsets.ModelViewSet):
    queryset = Criminal.objects.all()
    serializer_class = CriminalSerializer

class CriminalOffenseViewSet(viewsets.ModelViewSet):
    queryset = CriminalOffense.objects.all()
    serializer_class = CriminalOffenseSerializer