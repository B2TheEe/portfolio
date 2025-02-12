from django.urls import path

from . import views

app_name = "app_skills"
urlpatterns = [
    path("", views.get_all_skills, name="index"),
]