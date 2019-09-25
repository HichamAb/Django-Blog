from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import BlogPost
# Create your views here.

class HomePage(ListView) :
    queryset = BlogPost.objects.all()
    context_object_name = "posts"
    template_name = "home.html"

class PostDetail(DetailView) :
    model = BlogPost
    context_object_name = 'post'
    slug_url_kwarg = 'slug'
    template_name = 'post_detail.html'
