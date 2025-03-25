from django.contrib import admin
from .models import CrimeStat, CrimeStatSummary, CrimeTrend, CrimeHeatmap

class CrimeStatAdmin(admin.ModelAdmin):
    list_display = ('id', 'crime', 'criminal', 'offense', 'stat_date', 'stat_value')
    list_filter = ('stat_date',)
    search_fields = ('crime__description', 'criminal__first_name')

class CrimeStatSummaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'crime_type', 'crime_count', 'crime_rate', 'avg_sentence_length', 'recidivism_rate')
    list_filter = ('crime_type',)
    search_fields = ('crime_type',)

class CrimeTrendAdmin(admin.ModelAdmin):
    list_display = ('id', 'crime_type', 'trend_date', 'trend_value')
    list_filter = ('crime_type', 'trend_date')
    search_fields = ('crime_type',)

class CrimeHeatmapAdmin(admin.ModelAdmin):
    list_display = ('id', 'crime_type', 'location', 'crime_count')
    list_filter = ('crime_type', 'location')
    search_fields = ('crime_type', 'location')

admin.site.register(CrimeStat, CrimeStatAdmin)
admin.site.register(CrimeStatSummary, CrimeStatSummaryAdmin)
admin.site.register(CrimeTrend, CrimeTrendAdmin)
admin.site.register(CrimeHeatmap, CrimeHeatmapAdmin)