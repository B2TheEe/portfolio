from django.shortcuts import render
from .models import WorkExperience
# Create your views here.
def get_all_workexperience(request):
    workexperiences = WorkExperience.objects.all()
    print(workexperiences[0].name)
    print(workexperiences[0].description)
    print(workexperiences[1].name)
    print(workexperiences[1].description)

    context = {
        "workexperiences": workexperiences,
    }
    return render(request,template_name="work.html",context=context)
