from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from core.models import CrimeIncident, CriminalOffense, Criminal
from .models import CrimeStat, CrimeStatSummary, CrimeTrend, CrimeHeatmap
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.apps import apps
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from django.db import models

@receiver(post_save, sender=apps.get_model('core', 'CrimeIncident'))
def update_crime_stats(sender, instance, created, **kwargs):
    if not created:
        return

    # Dynamically get models to avoid circular import issues
    CrimeIncident = apps.get_model('core', 'CrimeIncident')
    CriminalOffense = apps.get_model('core', 'CriminalOffense')
    CrimeStat = apps.get_model('crimestats', 'CrimeStat')
    CrimeStatSummary = apps.get_model('crimestats', 'CrimeStatSummary')
    CrimeTrend = apps.get_model('crimestats', 'CrimeTrend')
    CrimeHeatmap = apps.get_model('crimestats', 'CrimeHeatmap')

    # Get first related offense
    offense = CriminalOffense.objects.filter(crime_incident=instance).first()

    if offense:
        crime_stat, _ = CrimeStat.objects.get_or_create(
            crime=instance,
            criminal=instance.criminals.first(),
            offense=offense
        )
        crime_stat.stat_date = instance.date_time.date()
        crime_stat.stat_value = 1 if offense.sentence_status == "convicted" else 0
        crime_stat.save()

    # Update CrimeStatSummary
    crime_count = CrimeIncident.objects.filter(crime_type=instance.crime_type).count()
    convicted_count = CriminalOffense.objects.filter(
        crime_incident__crime_type=instance.crime_type,
        sentence_status="convicted"
    ).count()

    crime_stat_summary, _ = CrimeStatSummary.objects.get_or_create(crime_type=instance.crime_type)
    crime_stat_summary.crime_count = crime_count
    crime_stat_summary.crime_rate = crime_count / 100000  # Assuming population
    crime_stat_summary.avg_sentence_length = CriminalOffense.objects.filter(
        crime_incident__crime_type=instance.crime_type
    ).aggregate(avg_sentence_length=models.Avg('sentence_length'))['avg_sentence_length'] or 0
    crime_stat_summary.recidivism_rate = (convicted_count / crime_count) * 100 if crime_count else 0
    crime_stat_summary.save()

    # Update CrimeTrend
    crime_trend, _ = CrimeTrend.objects.get_or_create(
        crime_type=instance.crime_type,
        trend_date=instance.date_time.date()
    )

    previous_trend = CrimeTrend.objects.filter(
        crime_type=instance.crime_type
    ).exclude(trend_date=instance.date_time.date()).order_by('-trend_date').first()

    prev_crime_count = previous_trend.crime_count if previous_trend else 0
    crime_trend.trend_value = ((crime_count - prev_crime_count) / prev_crime_count) * 100 if prev_crime_count else 0
    crime_trend.save()

    # Update CrimeHeatmap
    crime_heatmap, _ = CrimeHeatmap.objects.get_or_create(
        crime_type=instance.crime_type,
        location=instance.location
    )
    crime_heatmap.crime_count = CrimeIncident.objects.filter(
        crime_type=instance.crime_type,
        location=instance.location
    ).count()
    crime_heatmap.save()
