from django.db import models
from django.db import models

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length=250, default='')
    PublicationDate = models.DateTimeField(default='')
    body = models.TextField(max_length=500, default='')
    image = models.ImageField(upload_to='image/',default='')

    def __str__(self):
        return self.Title

    def summary(self):
        return self.body[:100]

    def PublicationDate_pretty(self):
        return self.PublicationDate.strftime('%b %e %Y')