from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.forms import PasswordChangeForm
from reward.forms import *
from django.contrib.auth import get_user_model
from reward.models import Reward, Student
import qrcode
import datetime
import time


def home(request):
    time = datetime.datetime.now()

    return render(request, 'index.html', locals())


def login(request):
    path = request.get_full_path()
    if request.method == 'POST':
        form = LoginForm(data=request.POST, auto_id="%s")
        if form.is_valid():
            data = form.clean()
            user = authenticate(username=data['username'].strip(), password=data['password'])
            auth_login(request, user)
            return redirect("home")

    else:
        form = LoginForm(auto_id="%s")

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
            auth_user = authenticate(username=username, password=password)
            auth_login(request, auth_user)
            return redirect("home")
    else:
        form = SignupForm(auto_id="%s")
    return render(request, 'signup.html', locals())


def change_password(request):
    path = request.get_full_path()
    if request.method == 'POST':
        form = ChangepwdForm(data=request.POST, auto_id="%s")
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                auth_user = authenticate(username=username, password=newpassword)
                auth_login(request, auth_user)
                return redirect("home")
            else:
                return render(request, 'change_password.html', {'form': form, 'oldpassword_is_wrong': True})
        else:
            return render(request, 'change_password.html', {'form': form})
    else:
        form = ChangepwdForm(auto_id="%s")
    return render(request, 'change_password.html', locals())


def logout_view(request):
    logout(request)
    return redirect('home')


def profile(request):

    return render(request, 'profile.html', locals())


def history(request):
    history = {'rewards': Reward.objects.filter(reward_object__username=request.user)}
    return render(request, 'history.html', history)


def chart_date(request):
    chart = {'rewards': Reward.objects.order_by('date')}
    return render(request, 'chart_date.html', chart)


def chart_activity(request):
    chart = {'rewards': Reward.objects.order_by('reward_name')}
    return render(request, 'chart_activity.html', chart)
