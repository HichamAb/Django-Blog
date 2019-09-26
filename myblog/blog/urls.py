from django.urls import path
from .views import HomePage,PostDetail,CreatePost

urlpatterns = [
    path('',HomePage.as_view(),name="home-page"),
    path('blogpost/<slug:slug>',PostDetail.as_view(),name="post-detail"),
    path('blogpost/newpost/',CreatePost.as_view(),name="create-post"),
]
