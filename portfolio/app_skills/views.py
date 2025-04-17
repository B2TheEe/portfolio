from django.views.decorators.csrf import csrf_protect

from .models import Skill,Category

from django.shortcuts import render

# Create your views here.
@csrf_protect
def get_all_skills(request):
    skills = Skill.objects.all()
    categories = Category.objects.all()
    context = {
        "skills": skills,
        "categories": categories,
    }
    return render(request,template_name="skills.html", context=context)

@csrf_protect
def get_skill(request,pk):
    skills = Skill.objects.all()
    skill = Skill.objects.get(pk=pk)
    categories = Category.objects.all()
    context = {
        "skills": skills,
        "categories": categories,
        "skill": skill,
    }
    return render(request, template_name="skills.html", context=context)
