from django.contrib import messages
from django.shortcuts import render
from blog.models import Post, PostTag
import datetime


# Create your views here.


def home_view(request):
    """messages.add_message(request, messages.INFO, 'Hello world.')
    messages.add_message(request, messages.INFO, 'Hello world.')
    messages.add_message(request,messages.ERROR, "fuck")
    messages.error(request, 'Email box full', extra_tags='email')"""
    posts = Post.objects.filter(published=True)
    return render(
        request,
        'blog/home.html',
        {'posts': posts}

    )


def about_view(request):
    """messages.add_message(request, messages.INFO, 'Hello world.')
    messages.add_message(request, messages.INFO, 'Hello world.')
    messages.add_message(request,messages.ERROR, "fuck")
    messages.error(request, 'Email box full', extra_tags='email')"""

    return render(
        request,
        'blog/about.html',
    )


def post_view(request, year, month, topic):

    post = Post.objects.get(topic=topic)
    return render(
        request,
        'blog/post.html',
        {'post': post, 'tags': PostTag.objects.filter(posts_id=post.id)}
    )
