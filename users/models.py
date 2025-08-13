from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from authentication.validators import validate_file_extension, validate_file_size

class HealthEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default = timezone.now)
    symptoms = models.TextField (blank=True)
    medications = models.TextField(blank=True)
    mood = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    attachment = models.FileField(upload_to='health_attachments/', null=True, blank=True, validators= [validate_file_extension, validate_file_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date'] # ordering descendign by the date field by default

    def __str__(self):
        return f"{self.user}"- {self.date}

        

