from email.policy import default

from django.db import models
from django.db.models import ForeignKey


# Create your models here.


# Create your models here
class Image(models.Model):
    caption =  models.CharField(max_length=50)
    image = models.ImageField(upload_to='images',help_text="Choose a picture for the landingpage")

    def __str__(self):
        return self.caption

    def image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s" />' % escape('media/inages/{}'.format(self.image.url))
        image_tag.short_description = 'Image'
        image_tag.allow_tags = True


class Document(models.Model):
    caption = models.CharField(max_length=50)
    document = models.FileField(db_index=True, upload_to='documents', help_text="Upload your CV!")

    def __str__(self):
        return self.caption


class SingletonModel(models.Model):
    _singleton = models.BooleanField(default=True, editable=False, unique=True)

    class Meta:
        abstract = True


class LandingPage(SingletonModel):
    picture = ForeignKey(Image, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, help_text="Title")
    subtitle = models.CharField(max_length=500, help_text="Subtitle")
    about = models.TextField(max_length=2500, help_text="About")
    gitHub_url = models.CharField(max_length=500, help_text="Github_url")
    linkedin_url = models.CharField(max_length=500, help_text="LinkedIn url")
    cv = ForeignKey(Document, on_delete=models.CASCADE)
    email = models.EmailField(help_text="How can people reach you?")
    phone_number = models.CharField(max_length=50, default=None, blank=True, null=True)