from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, ic):
    posts = Post.objects.get(id=ic)
    return render(request, 'posts.html', {'posts': posts})    
