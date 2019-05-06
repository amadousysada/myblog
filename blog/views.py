from django.contrib import messages
from django.shortcuts import render
import datetime


# Create your views here.


def home_view(request):
    """messages.add_message(request, messages.INFO, 'Hello world.')
    messages.add_message(request, messages.INFO, 'Hello world.')
    messages.add_message(request,messages.ERROR, "fuck")
    messages.error(request, 'Email box full', extra_tags='email')"""
    countdownStart = datetime.datetime(2019, 5, 10,00, 00)
    countdownNow = countdownStart-datetime.datetime.now()
    date = computeTimeStamp(countdownNow.seconds)
    return render(
        request,
        'blog/home.html',
        {"date":date,"countdown":countdownNow}
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

def computeTimeStamp(countdown):

    hours = countdown // 3600 if (countdown // 3600)>9 else "0"+str((countdown // 3600))

    minutes = (countdown % 3600)//60 if (countdown // 60)>9 else "0"+str((countdown // 60))

    seconds = (countdown % 3600)%60 if ((countdown % 3600)%60)>9 else "0"+str((countdown % 3600)%60)

    attributes = { 'hours': hours, 'minutes': minutes, 'seconds': seconds }
    date = dateObject(attributes)
    return date

class dateObject():
    """docstring for ClassName"""
    def __init__(self, initial_attrs):
        for key in initial_attrs:
            setattr(self, key, initial_attrs[key])
        