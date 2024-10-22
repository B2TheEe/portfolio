from django.shortcuts import render
from django.utils.translation.template import context_re
from .models import AboutMe


# Create your views here.
def about_me_view(request):
    about_me_data = AboutMe.objects.get(pk=1)
    data = {
        "test": "test",
        "about_me": about_me_data,
    }
    return render(request, template_name="about-me.html",context=data)