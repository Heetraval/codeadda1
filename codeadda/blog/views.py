from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import redirect
from blog.models import Post, BlogComment
from django.contrib import messages


def blogHome(request, slug):
    allposts = Post.objects.all()
    #print(allposts)
    context = {'allposts': allposts}
    return render(request, 'blog/bloghome.html', context)



def blogPost(request):
    post = Post.objects.filter().first()
    comments = BlogComment.objects.filter(post=post)
    context = {'post' : post , 'comments' : comments}
      
    return render(request, 'blog/blogpost.html', context)



def postcomment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postsno = request.POST.get("postsno")
        post = Post.objects.get()
        
        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages.success(request, "Your comment has been added")
        #print(comment)
    return redirect("/bloghome")


def blog(request):
    return render(request, 'blog/blog.html')
# Create your views here.
def blog1(request):
    return render(request, 'blog/blog1.html')