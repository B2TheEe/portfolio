from django.db import models

# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name
class Tag(models.Model):
    tag = models.CharField(max_length=100)

class BlogArticle(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='media/')
    text = models.TextField(max_length=1500)
    date_published = models.DateTimeField()
    date_modified = models.DateTimeField()
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return  self.title