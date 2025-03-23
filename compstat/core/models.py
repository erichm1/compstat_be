import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save, m2m_changed  # Import pre_save and m2m_changed here
from django.dispatch import receiver
from django.contrib.gis.db import models as gis_models

class CrimeIncident(models.Model):
    CRIME_DATA_CHOICES = (
        ("theft", "theft"),
        ("assault", "assault"),
        ("vandalism", "vandalism"),
        ("fraud", "fraud"),
        ("embezzlement", "embezzlement"),
        ("forgery", "forgery"),
        ("identity_fraud", "identity fraud"),
        ("defamation", "defamation"),
        ("libel", "libel"),
        ("slander", "slander"),
        ("trespassing", "trespassing"),
        ("identity_theft", "identity theft"),
        ("counterfeiting", "counterfeiting"),
        ("copyright_infringement", "copyright infringement"),
        ("smuggling", "smuggling"),
        ("tax_evasion", "tax evasion"),
        ("illegal_gambling", "illegal gambling"),
        ("bribery_passive", "bribery (passive)"),
        ("bribery_active", "bribery (active)"),
        ("unlawful_sale_of_goods", "unlawful sale of goods"),
        ("money_laundering", "money laundering"),
        ("environmental_violation", "environmental violation"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    crime_type = models.CharField(max_length=100, choices=CRIME_DATA_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=100)
    reported_by = models.CharField(max_length=100)
    precinct = models.CharField(max_length=10, null=True, blank=True)
    admin_district = models.CharField(max_length=100, null=True, blank=True)
    criminals = models.ManyToManyField('Criminal', related_name="crimes", blank=True)
    #latitude = models.FloatField()
    #longitude = models.FloatField()
    #point = gis_models.PointField(geography=True, null=True, blank=True)
    date_time = models.DateTimeField()
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


class Criminal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    alias = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[
        ("male", "male"),
        ("female", "female"),
        ("other", "other"),
    ])
    nationality = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    national_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    last_known_location = models.CharField(max_length=255, null=True, blank=True)
    arrest_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Criminals"


class CriminalOffense(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    criminal = models.ForeignKey('Criminal', on_delete=models.CASCADE)
    crime_incident = models.ForeignKey('CrimeIncident', on_delete=models.CASCADE)
    offense_date = models.DateTimeField()
    sentence_status = models.CharField(max_length=50, choices=[
        ("under_investigation", "Under Investigation"),
        ("charged", "Charged"),
        ("convicted", "Convicted"),
        ("acquitted", "Acquitted"),
    ], default="under_investigation")
    process_number = models.CharField(max_length=50, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ("criminal", "crime_incident")  # Avoid duplicates
        verbose_name_plural = "Offenses"

    def __str__(self):
        return f"{self.criminal.first_name} - {self.crime_incident.crime_type}"

# Signal to create a process number when sentence status is 'charged', 'convicted', or 'acquitted'
@receiver(pre_save, sender=CriminalOffense)
def generate_process_number(sender, instance, **kwargs):
    # Check if the status is one of the relevant ones and if process_number is empty
    if instance.sentence_status in ['charged', 'convicted', 'acquitted'] and not instance.process_number:
        # Generate a unique process number, here it's an example, you can customize the logic
        instance.process_number = f"COMPSTAT{uuid.uuid4().hex[:8].upper()}"


# Signal to create CriminalOffense automatically when criminals are associated with a CrimeIncident
@receiver(m2m_changed, sender=CrimeIncident.criminals.through)
def create_criminal_offenses(sender, instance, action, reverse, model, pk_set, **kwargs):
    # Only handle when criminals are added to a crime incident
    if action == "post_add":
        for criminal_id in pk_set:
            criminal = Criminal.objects.get(id=criminal_id)
            # Check if there's already an offense for this criminal and this crime incident
            if not CriminalOffense.objects.filter(criminal=criminal, crime_incident=instance).exists():
                # Create the CriminalOffense for the new association
                CriminalOffense.objects.create(
                    criminal=criminal,
                    crime_incident=instance,
                    offense_date=instance.date_time,
                    sentence_status="under_investigation"  # Default status
                )