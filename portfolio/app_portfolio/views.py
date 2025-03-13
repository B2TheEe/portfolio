from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView
from haystack.query import SearchQuerySet
from taggit.models import Tag

from .models import PortfolioItem
# Create your views here.

def get_all_portfolio_items(request):
    portfolioitem_list = PortfolioItem.objects.all()
    tags = Tag.objects.filter(portfolioitem__in=portfolioitem_list).distinct()
    paginator = Paginator(portfolioitem_list, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "portfolioitem_list": portfolioitem_list,
        "tags": tags,
        "page_obj": page_obj,
    }
    return render(request,template_name="portfolio.html",context=context)

def get_portfolio_item(request, pk):
    portfolio_item = PortfolioItem.objects.get(pk=pk)
    context = {
        "portfolioitem": portfolio_item
    }
    return render(request,template_name="portfolio-item.html", context=context)

def get_tag(request,tag):
    tag_pk = Tag.objects.get_by_natural_key(tag)
    portfolioitem_list = PortfolioItem.objects.filter(tags=tag_pk)

    context = {
        "tag": tag_pk,
        "portfolioitem_list": portfolioitem_list,
    }
    return render(request,template_name="portfolio-tag.html", context=context)