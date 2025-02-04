from django.urls import path

from .views import index

app_name = 'app_skills'
urlpatterns = [
    path('', index, name='chack_out')
]