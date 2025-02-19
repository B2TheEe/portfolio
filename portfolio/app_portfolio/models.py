from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class PortfolioItem(models.Model):
  photo = models.ImageField(upload_to='media/')
  name = models.CharField(max_length=100)
  gitHubUrl = models.CharField(max_length=100)
  description = models.TextField(max_length=1000)
  tags = TaggableManager()

  def __str__(self):
    return self.name
