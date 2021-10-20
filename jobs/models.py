from django.db import models

# Create your models here.
class Job(models.Model):
    imagesfun = models.ImageField(upload_to='image/', default='')
    summary = models.CharField(max_length=200, default='')
