from django.db import models


# Create your models here.
class Category(models.Model):
    name =  models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    Rating_CHOICES = (
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    )
    skill = models.CharField(max_length=100)
    rating = models.IntegerField(choices=Rating_CHOICES, default=1)
    description = models.TextField(max_length=1000,default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill





