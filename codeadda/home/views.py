from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.db import IntegrityError


def blogpost(request):
    return render(request, 'home/index.html')


def contact(request):
    messages.success(request, 'Welcome')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill correctly")

        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(request, "Your form has been filled")

    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allposts = Post.objects.none()
    else:
        allpoststitle = Post.objects.filter(title__icontains=query)
    allpostscontent = Post.objects.filter(content__icontains=query)
    allposts = allpoststitle.union(allpostscontent)
    params = {'allposts': allposts, 'query': query}

    return render(request, 'home/search.html', params)

    return HttpResponse("heyookooojo")


def profile(request):
    return render(request, 'home/profile.html')
    
def signup(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')




        #myuser = User.objects.create_user(username, email , password)
        myuser = User.objects.create_user(username, email, password)
        #myuser_username = username
        #myuser_email = email
        #myuser_password = password
        #myuser = form.save(commit = False)
        myuser.save()
        messages.success(request, "Your Account has been Successfully created")
        
    else:
        return HttpResponse("404 Not Found")  

        


# Create your views here.
