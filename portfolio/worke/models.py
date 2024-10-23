from importlib.metadata import requires

from django.db import models

# Create your models here.
class WorkExperience(models.Model):
    photo = models.ImageField(upload_to='media/')
    company = models.CharField(max_length=100,default=None)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    from_date = models.DateField()
    to_date = models.DateField()