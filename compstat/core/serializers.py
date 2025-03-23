from rest_framework import serializers
from .models import CrimeIncident, Criminal, CriminalOffense


class CriminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Criminal
        fields = '__all__'


class CrimeIncidentSerializer(serializers.ModelSerializer):
    criminals = CriminalSerializer(many=True, read_only=True)
    class Meta:
        model = CrimeIncident
        fields = '__all__'


class CriminalOffenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriminalOffense
        fields = '__all__'