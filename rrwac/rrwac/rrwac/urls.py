"""rrwac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from reward import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.SignUp, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('history/', views.history, name='history'),
    path('chart_date/', views.chart_date, name='chart_date'),
    path('chart_activity/', views.chart_activity, name='chart_activity'),
    path('get_all_users/', views.get_all_users, name='get_all_users'),
    path('get_single_user/<int:user_id>/', views.get_single_user, name='get_single_user'),
    path('get_all_rewards/', views.get_all_rewards, name='get_all_rewards'),
]
