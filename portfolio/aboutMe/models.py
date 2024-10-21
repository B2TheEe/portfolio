from django.db import models
from phonenumber_field.formfields import PhoneNumberField


# Create your models here.
class SingletonModel(models.Model):
    _singleton = models.BooleanField(default=True, editable=False, unique=True)

    class Meta:
        abstract = True


class AboutMe(SingletonModel):
    photo = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_number = PhoneNumberField()
    email_address = models.EmailField()
    github = models.CharField(max_length=250)
    linkedIn = models.CharField(max_length=250)
    about_me = models.TextField(max_length=1500)