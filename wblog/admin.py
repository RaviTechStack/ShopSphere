from django.contrib import admin
from .models import Allproducts, profile, Comment

# Register your models here.
admin.site.register((Allproducts, profile, Comment))