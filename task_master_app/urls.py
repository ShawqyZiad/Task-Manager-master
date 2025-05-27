"""Task_Master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('login', views.loginPage),
    path('process_login', views.process_login),
    path('process_logout', views.process_logout),
    path('signup', views.signupPage),
    path('process_signup', views.process_signup),
    path('teams', views.teams),
    path('tasks', views.tasks),
    path('tasks-employee', views.tasks_employee),
]
