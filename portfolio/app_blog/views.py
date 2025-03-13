from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import BlogArticle
from taggit.models import Tag
from .search_indexes import BlogArticleIndex

# Create your views here.
def get_all_blogs(request):
    blogs = BlogArticle.objects.filter(status=1)
    tags = Tag.objects.filter(blogarticle__in=blogs)
    paginator = Paginator(blogs, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "blogs": blogs,
        "tags": tags,
        "page_obj": page_obj,
    }
    return render(request,"blogarticles.html",context=context)


def get_blog(request, pk):
    blogarticle = BlogArticle.objects.get(pk=pk)
    context = {
        "blog": blogarticle,
    }
    return render(request,template_name="blogarticle.html", context=context)


def get_tag(request,tag):
    print(tag)

    tag_pk = Tag.objects.get_by_natural_key(tag)
    print(tag_pk)
    blogs = BlogArticle.objects.filter(tags=tag_pk)


    context = {
        "tag": tag_pk,
        "blogs": blogs,
    }
    return render(request,template_name="blogarticles-tag.html", context=context)

def search(request):
    blogs_list = BlogArticle.objects.all()
    blogs_filter = BlogArticleFilter(request.GET, queryset=blogs_list)
    return render(request, 'search/user_list.html', {'filter': blogs_filter})