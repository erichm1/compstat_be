from django.contrib import admin
from .models import CrimeIncident

@admin.register(CrimeIncident)
class CrimeIncidentAdmin(admin.ModelAdmin):
    list_display = ('id','crime_type', 'location', 'date_time', 'reported_by')
    list_filter = ('crime_type', 'location', 'date_time', 'reported_by')
    search_fields = ('id','crime_type', 'location', 'reported_by')
    readonly_fields = ('created_at', 'updated_at')