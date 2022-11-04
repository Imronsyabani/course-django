from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from .forms import SignIN
from . import models
# Create your views here.

def index(request):
    return render(request,'login/index.html')

def sign_in(request):
    if request.method == 'POST':
        form = SignIN(request.POST)
        if form.is_valid:
            if models.User.objects.filter(email__exact=form.data['email']):
                request.session['_redirect_admin'] = True
                return HttpResponseRedirect('/admin',request)
            else:
                context = {'warning_auth':True}
                requests = HttpRequest()
                requests.META = request.META
                requests.method = 'GET'
                requests.META['SERVER_NAME'] = request.META['SERVER_NAME']
                requests.path = '/login'
                requests.path_info = '/login'
                return render(requests,'login/index.html',context)
    return HttpResponseRedirect('/')

def sign_up(request):
    if request.method == 'POST':
        form = SignIN(request.POST)
        if form.is_valid:
            result = models.User.create_object(form.data)
            return HttpResponseRedirect('/login')
    return HttpResponseRedirect('/')