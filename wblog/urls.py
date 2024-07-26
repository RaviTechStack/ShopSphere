from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("categories/<cat>", views.categories),
    path("detailpro/<slug>", views.detailpage),
    path("cart", views.showCart),
    path("search", views.search),
    path("signin", views.signin),
    path("signup", views.signup),
    path("logout", views.logout),
    path("order", views.showOrderPage)
]
