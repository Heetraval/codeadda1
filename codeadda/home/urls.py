from django.urls import path
from . import views



urlpatterns = [
    path('', views.blogpost , name="blogpost"),
    path('contact', views.contact , name="contact"),
    path('about/', views.about , name="about"),
    path('search', views.search, name="search"),
    path('about/profile', views.profile, name="profile"),
    path('signup', views.signup, name="signup")
]