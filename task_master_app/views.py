from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from . import *
import bcrypt



def home(request):
    return render(request, 'home.html')

def loginPage(request):
    if 'user_id' in request.session:
        return redirect('/')
    else:
        return render(request, 'login.html')

def process_login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    else:
        user = User.objects.filter(email = request.POST['email'])
        request.session['user_id'] = user[0].id
        return redirect('/')

def process_logout(request):
    request.session.flush()
    return redirect('/')

def signupPage(request):
    if 'user_id' in request.session:
        return redirect('/')
    else:
        return render(request, 'signup.html')

def process_signup(request):
    errors = User.objects.signup_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/signup')
    else:
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            company = request.POST['company'],
            permission_level = request.POST['permission_level'],
            email = request.POST['email'],
            password = pw_hash
            )
    request.session['user_id'] = user.id
    return redirect('/')
        

def teams(request):
    # Matthew's part
    return render(request, 'teams.html')

def tasks(request):
    return render(request, 'tasks-admin.html')

def tasks_employee(request): 
    return render(request, 'tasks-employee.html')
    # This is a temporary function to load tasks-employee.html, when working on the backend of the project, we can make an "if" statement in previous function that says if user.permission_level == 1, display tasks-employees.html else if user.permission_level == 8 or 9, then display tasks-admin.html
