from django.urls import path
from . import views

app_name = "app_blog"

urlpatterns = [
    path("", views.get_all_blogs, name="index"),
]