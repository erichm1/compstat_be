import uuid
from django.db import models
from django.contrib.gis.db import models as gis_models

class CrimeIncident(models.Model):
    CRIME_DATA_CHOICES = (
        ("theft", "theft"),
        ('assault', 'assault'),
        ("vandalism", "vandalism"),
        ("fraud", "fraud"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    crime_type = models.CharField(max_length=100, choices=CRIME_DATA_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    reported_by = models.CharField(max_length=100)
    #latitude = models.FloatField()
    #longitude = models.FloatField()
    #point = gis_models.PointField(geography=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #def save(self, *args, **kwargs):
    #    if self.latitude and self.longitude:
    #        from django.contrib.gis.geos import Point
    #        self.point = Point(self.longitude, self.latitude)
    #    super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id).replace("-", "-")

    def created_at_str(self):
        return self.created_at.strftime("%Y-%m-%d %H:%M:%S")

    def updated_at_str(self):
        return self.updated_at.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        verbose_name_plural = "Crimes"