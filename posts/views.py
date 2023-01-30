from django.shortcuts import render
from .models import Post

# Create your views here.

#homepage
def index(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {'posts':posts}) #pass all posts to index.html

def post(request, pk):
    posts = Post.objects.get(id=pk) #once you go to post/1, find the post
    return render(request, 'posts.html', {'posts':posts} ) #pass it to post.html to display that specific post