from django.contrib import admin
from .models import CrimeIncident, Criminal, CriminalOffense

@admin.register(CrimeIncident)
class CrimeIncidentAdmin(admin.ModelAdmin):
    list_display = ('id','crime_type', 'location', 'admin_district', 'precinct','date_time', 'reported_by')
    list_filter = ('crime_type', 'location', 'date_time', 'reported_by')
    search_fields = ('id','crime_type', 'location', 'reported_by')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('criminals',)


@admin.register(Criminal)
class CriminalAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'birth_date')
    list_filter = ('id', 'first_name', 'last_name', 'alias')
    search_fields = ('id','first_name', 'last_name', 'alias')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(CriminalOffense)
class CriminalOffenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'criminal', 'crime_incident', 'offense_date', 'sentence_status', 'process_number')
    list_filter = ('criminal', 'crime_incident', 'process_number', 'sentence_status')
    search_fields = ('id', 'process_number', 'sentence_status')
    readonly_fields = ('created_at', 'updated_at')