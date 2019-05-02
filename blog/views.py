from django.contrib import messages
from django.shortcuts import render

# Create your views here.


def home_view(request):
    """messages.add_message(request, messages.INFO, 'Hello world.')
    messages.add_message(request, messages.INFO, 'Hello world.')
    messages.add_message(request,messages.ERROR, "fuck")
    messages.error(request, 'Email box full', extra_tags='email')"""

    return render(
        request,
        'blog/home.html',
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
