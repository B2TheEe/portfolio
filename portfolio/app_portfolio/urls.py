from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_all_portfolio_items, name="index"),
    path("/<pk>", views.get_portfolio_item, name="portfolio-item")
]