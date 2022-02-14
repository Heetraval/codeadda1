from django.urls import path
from . import views



urlpatterns = [
    path('bloghome/postcomment', views.postcomment, name="postcomment"),
    path('', views.blogPost, name="blogPost"),

    path('<str:slug>', views.blogHome, name="blogHome"),
    path('bloghome/blog', views.blog, name="blog"),
    path('bloghome/blog-1', views.blog1, name="blog-1")



   
]