from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    return render(request, 'home.html', {})


def logIn(request):

    return render(request, 'logIn.html', {})


def signUp(request):

    return render(request, 'signUp.html', {})


def profile(request):

    return render(request, 'profile.html', {})


def history(request):

    return render(request, 'history.html', {})


def chart(request):

    return render(request, 'chart.html', {})
