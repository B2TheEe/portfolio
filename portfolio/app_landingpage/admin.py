from django.contrib import admin

from .models import LandingPage, Document, Image

# Register your models here.
admin.site.register(LandingPage)
admin.site.register(Document)
admin.site.register(Image)