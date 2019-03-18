from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import BlogArtcle
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    blogs = BlogArtcle.objects.all()
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return render(request,'main.html',context={'blogs':blogs,'user': user})
    return render(request,'main.html',context={'blogs':blogs,'user': None})


def createBlog(request):
    b1 = BlogArtcle()
    b1.title=request.POST['title']
    b1.author=request.user 
    user=b1.author
    b1.blog_content=request.POST['blog_content']
    b1.save()
    blogs = BlogArtcle.objects.all()
    return render(request,'main.html',context={'blogs':blogs,'user': user})
    
