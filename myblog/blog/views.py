from django.shortcuts import render
from django.views.generic import ListView

from .models import BlogPost
# Create your views here.

class HomePage(ListView) :
    queryset = BlogPost.objects.all()
    context_object_name = "posts"
    template_name = "home.html"

