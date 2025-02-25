from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

    """ 
class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

"""

class BlogArticle(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='media/')
    summary = models.TextField(max_length=150,default="")
    text = models.TextField(max_length=15000)
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField()
    status = models.IntegerField(choices=STATUS, default=0)
    tags = (TaggableManager())
    def __str__(self):
        return  self.title