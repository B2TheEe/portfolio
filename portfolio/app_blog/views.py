from django.shortcuts import render
from django.core.paginator import Paginator
from .models import BlogArticle

# Create your views here.
def get_all_blogs(request):
    blogs = BlogArticle.objects.filter(status=1)
    paginator = Paginator(blogs, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "blogs": blogs,
        "page_obj": page_obj,
    }
    return render(request,"blogarticles.html",context=context)

def get_blog(request, pk):
    blogarticle = BlogArticle.objects.get(pk=pk)
    context = {
        "blog": blogarticle,
    }
    return render(request,template_name="blogarticle.html", context=context)

