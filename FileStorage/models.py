from django.db import models

class Upload(models.Model):
  file = models.FileField(blank=False, null=False)
  remarks=models.CharField(max_length=100)
  