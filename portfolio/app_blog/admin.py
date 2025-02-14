from django.contrib import admin
from .models import BlogArticle, Author,Tag

# Register your models here.
admin.site.register(BlogArticle)
admin.site.register(Author)
admin.site.register(Tag)
