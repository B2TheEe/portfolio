from django.contrib import admin
from .models import SingletonModel,AboutMe

admin.site.register(SingletonModel)
admin.site.register(AboutMe)
