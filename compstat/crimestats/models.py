# models.py
from django.db import models
from core.models import CrimeIncident, Criminal, CriminalOffense
from crimestats.signals import update_crime_stats

class CrimeStat(models.Model):
    crime = models.ForeignKey(CrimeIncident, on_delete=models.CASCADE, related_name='crime_stats')
    criminal = models.ForeignKey(Criminal, on_delete=models.CASCADE, related_name='crime_stats')
    offense = models.ForeignKey(CriminalOffense, on_delete=models.CASCADE, related_name='crime_stats')
    stat_date = models.DateField()
    stat_value = models.IntegerField()

    def __str__(self):
        return f"{self.crime} - {self.criminal} - {self.offense} - {self.stat_date}"

    def save(self, *args, **kwargs):
        self.stat_date = self.crime.date_time.date()
        self.stat_value = 1 if self.offense.sentence_status == "convicted" else 0
        super().save(*args, **kwargs)

class CrimeStatSummary(models.Model):
    crime_type = models.CharField(max_length=255)  # e.g. "Violent", "Property", etc.
    crime_count = models.IntegerField()
    crime_rate = models.DecimalField(max_digits=5, decimal_places=2)  # per 100,000 population
    avg_sentence_length = models.DecimalField(max_digits=5, decimal_places=2)  # in months
    recidivism_rate = models.DecimalField(max_digits=5, decimal_places=2)  # percentage

    def __str__(self):
        return f"{self.crime_type} - {self.crime_count} - {self.crime_rate}%"

    def save(self, *args, **kwargs):
        crime_incidents = CrimeIncident.objects.filter(crime_type=self.crime_type)
        self.crime_count = crime_incidents.count()
        self.crime_rate = (self.crime_count / 100000)  # assuming a population of 100,000
        self.avg_sentence_length = CriminalOffense.objects.filter(crime_incident__in=crime_incidents).aggregate(avg_sentence_length=models.Avg('sentence_length'))['avg_sentence_length']
        self.recidivism_rate = (CriminalOffense.objects.filter(crime_incident__in=crime_incidents, sentence_status="convicted").count() / self.crime_count) * 100
        super().save(*args, **kwargs)

class CrimeTrend(models.Model):
    crime_type = models.CharField(max_length=255)  # e.g. "Violent", "Property", etc.
    trend_date = models.DateField()
    trend_value = models.DecimalField(max_digits=5, decimal_places=2)  # percentage change from previous period

    def __str__(self):
        return f"{self.crime_type} - {self.trend_date} - {self.trend_value}%"

    def save(self, *args, **kwargs):
        previous_trend = CrimeTrend.objects.filter(crime_type=self.crime_type).order_by('-trend_date').first()
        self.trend_value = ((self.crime_count - previous_trend.crime_count) / previous_trend.crime_count) * 100
        super().save(*args, **kwargs)

class CrimeHeatmap(models.Model):
    crime_type = models.CharField(max_length=255)  # e.g. "Violent", "Property", etc.
    location = models.CharField(max_length=255, null=True, blank=True)
    crime_count = models.IntegerField()

    def __str__(self):
        return f"{self.crime_type} - {self.location} - {self.crime_count}"

    def save(self, *args, **kwargs):
        crime_incidents = CrimeIncident.objects.filter(crime_type=self.crime_type, location=self.location)
        self.crime_count = crime_incidents.count()
        super().save(*args, **kwargs)