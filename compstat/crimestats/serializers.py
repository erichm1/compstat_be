from rest_framework import serializers
from .models import CrimeStat, CrimeStatSummary, CrimeTrend, CrimeHeatmap

class CrimeStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeStat
        fields = '__all__'

class CrimeStatSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeStatSummary
        fields = '__all__'

class CrimeTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeTrend
        fields = '__all__'

class CrimeHeatmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeHeatmap
        fields = '__all__'