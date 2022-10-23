from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import random

from blog.models import Post

from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def index(request):
    all_posts = Post.objects.filter(status=Post.ACTIVE)
    categories = get_categories(all_posts)
    return render(request, 'core/index.html', {"all_posts": all_posts, "categories":categories })

def get_posts():
    all_posts = Post.objects.filter(status=Post.ACTIVE)
    return all_posts

def get_categories(post_list):
    categories = []
    for post in post_list :
        if post.get_category() not in categories :
            categories.append(post.get_category())
    return categories

# def frontpage(request):
#     posts = Post.objects.filter(status=Post.ACTIVE)
#     return render(request, 'core/frontpage.html', {"posts": posts })

def about(request):
    return render(request, 'core/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]

    return HttpResponse("\n".join(text), content_type="text/plain")