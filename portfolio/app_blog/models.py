from django.db import models

# Create your models here.
class BlogArticle(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1500)
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField()
    picture = models.ImageField(upload_to='media/')