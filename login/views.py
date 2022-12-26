from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpRequest as rq
from .forms import SignIN,SignUP
from . import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import hashers,login
# Create your views here.

def index(request):
    if request.method == 'POST':
        
        is_admin,form = sign_in(request,'is_admin')
        is_user,form = sign_in(request)
        if is_admin:
            request.session['_redirect_admin'] = True
            request.user = User.objects.get(Q(email=form.data['email']))
            login(request,user=request.user)
            return HttpResponseRedirect('/admin',request)
        elif is_user:
            return HttpResponseRedirect('/',request)
        else:
            context = {'warning_auth':True}
            return render(request,'login/index.html',context)
    return render(request,'login/index.html')

def sign_in(request,user_level='is_user'):
    if request.method == 'POST':
        form = SignIN(request.POST)
        if form.is_valid:        
            if models.DetailUser._valid_login_admin(form.data['email'],form.data['password']) and user_level == 'is_admin':
                return (True,form)
            elif models.DetailUser._valid_login_user(form.data['email'],form.data['password']) and user_level == 'is_user':
                return (True,form)
            else:
                return (False,form)

def valid_form(data):
    user_exist = User.objects.filter(username=data['username'])
    user_email_exist = User.objects.filter(email=data['email'])
    return (user_exist, user_email_exist)
    

def register(request):
    if request.method == 'POST':
        result = sign_up(request)
        if isinstance(result, User):
            render(request, 'login/index.html')
        else:
            return result
    return render(request,'login/register.html')
    
def sign_up(request):
    if request.method == 'POST':
        form = SignUP(request.POST)
        if form.is_valid:
            can_create = valid_form(form.data)
            username = "Username Has Already Exist" if can_create and can_create[0] else ''
            email = "Email Has Already Exist" if can_create and can_create[1] else ''
            if not any(can_create):
                return models.DetailUser.create_object(form.data)
            else:
                return render(request, 'login/register.html',context={'warning_auth':True,'username_error':username, 'email_error':email})
            # return HttpResponseRedirect('/login')
    return HttpResponseRedirect('/')