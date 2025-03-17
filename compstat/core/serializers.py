from rest_framework import serializers
from .models import CrimeIncident

class CrimeIncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeIncident
        fields = '__all__'