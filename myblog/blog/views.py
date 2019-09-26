from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
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


class CreatePost(LoginRequiredMixin,CreateView):
    model = BlogPost
    fields = ["title","content"]
    template_name = "create_post.html"
    success_url = "/"

    def form_valid(self,form) :
            form.instance.author=self.request.user
            return super().form_valid(form)