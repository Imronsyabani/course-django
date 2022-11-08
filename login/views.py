from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpRequest as rq
from .forms import SignIN,SignUP
from . import models
from django.contrib.auth import hashers
# Create your views here.

def index(request):
    if request.method == 'POST':
        if sign_in(request):
            request.session['_redirect_admin'] = True
            return HttpResponseRedirect('/admin',request)
        else:
            context = {'warning_auth':True}
            return render(request,'login/index.html',context)
    return render(request,'login/index.html')

def sign_in(request):
    if request.method == 'POST':
        form = SignIN(request.POST)
        if form.is_valid:        
            if models.User._valid_login(form.data['email'],form.data['password']):
                return True
            else:
                return False

def sign_up(request):
    if request.method == 'POST':
        form = SignUP(request.POST)
        if form.is_valid:
            result = models.User.create_object(form.data)
            return HttpResponseRedirect('/login')
    return HttpResponseRedirect('/')