from django.shortcuts import render
from django.http import request,HttpResponseRedirect
from .forms import SignIN
# Create your views here.

def index(request):
    return render(request,'login/index.html')

def sign_in(request):
    if request.method == 'POST':
        form = SignIN(request.POST)
        if form.is_valid:
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def sign_up(request):
    if request.method == 'POST':
        form = SignIN(request.POST)
        if form.is_valid:
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')