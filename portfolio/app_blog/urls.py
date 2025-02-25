from django.urls import path, re_path
from . import views

app_name = "app_blog"

urlpatterns = [
    path("", views.get_all_blogs, name="index"),
    path("/<pk>", views.get_blog, name="blog"),
    path('/tag/<tag>', views.get_tag , name="get-tag"),
]