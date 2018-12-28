from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
import datetime
from django.contrib.auth import authenticate, login as auth_login, logout
from reward.forms import SignupForm
from django.contrib.auth import get_user_model
import qrcode


def home(request):
    time = datetime.datetime.now()

    return render(request, 'index.html', locals())


def login(request):

    return render(request, 'login.html', locals())


def SignUp(request):
    path = request.get_full_path()
    if request.method == 'POST':
        form = SignupForm(data=request.POST, auto_id="%s")
        if form.is_valid():
            UserModel = get_user_model()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            id = form.cleaned_data['id']
            password = form.cleaned_data['password']
            user = UserModel.objects.create_user(username=username, email=email, id=id, password=password)
            user.save()
            auth_user = authenticate(email=email, password=password)
            auth_login(request, auth_user)
            return redirect("home")
    else:
        form = SignupForm(auto_id="%s")
    return render(request, 'signup.html', locals())


def profile(request):

    return render(request, 'profile.html', locals())


def history(request):

    return render(request, 'history.html', locals())


def chart(request):

    return render(request, 'chart.html', locals())
