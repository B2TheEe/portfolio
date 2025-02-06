from importlib.metadata import requires

from django.db import models

# Create your models here.
class EducationExperience(models.Model):
    photo = models.ImageField(upload_to='media/')
    company = models.CharField(max_length=100,default=None)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    from_date = models.DateField()
    to_date = models.DateField()
    Propaedeutic_exam_date = models.DateField(default=None,blank=True,null=True )
    degree_date = models.DateField(default=None,blank=True,null=True )

    def __str__(self):
        return self.name + "\t" + self.company

