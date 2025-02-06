from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class SingletonModel(models.Model):
    _singleton = models.BooleanField(default=True, editable=False, unique=True)

    class Meta:
        abstract = True


class AboutMe(SingletonModel):
    photo = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=50,default=None)
    email_address = models.EmailField(_())
    github = models.CharField(max_length=250)
    linkedIn = models.CharField(max_length=250)
    about_me = models.TextField(_(max_length=1500))

    def __str__(self):
        return self.name
