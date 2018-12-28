from django.shortcuts import render
from django.http import HttpResponse
import qrcode


def home(request):
    idk = qrcode.make('1125029')
    return render(request, 'home.html', locals())


def logIn(request):

    return render(request, 'logIn.html', locals())


def signUp(request):

    return render(request, 'signUp.html', locals())


def profile(request):

    return render(request, 'profile.html', locals())


def history(request):

    return render(request, 'history.html', locals())


def chart(request):

    return render(request, 'chart.html', locals())
