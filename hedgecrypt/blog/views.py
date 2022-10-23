from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Post, Category
from .forms import CommentForm
import random

def get_posts():
    all_posts = Post.objects.filter(status=Post.ACTIVE)
    return all_posts

def get_random_posts(i):
    random_posts = random.sample(list(get_posts()), i)
    return random_posts

def get_categories(post_list):
    categories = []
    for post in post_list :
        if post.get_category() not in categories :
            categories.append(post.get_category())
    return categories

def get_first():
    return Post.objects.order_by('created_at').first()

def get_last():
    return Post.objects.order_by('created_at').last()

def home(request):
    all_posts = Post.objects.filter(status=Post.ACTIVE)
    categories = get_categories(all_posts)
    random_posts = get_random_posts(3)
    first = get_first()
    last = get_last()

    return render(request, 'blog/home.html', {"all_posts": all_posts, "categories": categories, "random_posts":random_posts, "first": first, "last": last})

def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)

    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_detail", category_slug=category_slug, slug=slug)

    else :
        form = CommentForm()

    return render(request, "blog/post-detail.html", {"post":post, "form": form})

def privacy_policy(request):
    return render(request, "blog/privacy_policy.html")

def terms_conditions(request):
    return render(request, "blog/terms_conditions.html")


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    all_posts = Post.objects.filter(status=Post.ACTIVE)
    categories = get_categories(get_posts())
    random_posts = get_random_posts(3)
    return render(request, "blog/category.html", {"category":category, "posts":posts, "all_posts":all_posts, "categories": categories, "random_posts":random_posts})


def search(request):
    query = request.GET.get("query", "")
    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))
    return render(request, 'blog/search.html', {"posts":posts, "query":query})



