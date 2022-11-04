from django.shortcuts import render
from django.views import defaults
from django.http import request,HttpResponseRedirect
# Create your views here.
def index(request,exception=None):
    return defaults.page_not_found(request,template_name='404.html')

def dashboard(request):
    if request.session.get('_redirect_admin'):
        return render(request,'dashboard.html')
    else:
        return HttpResponseRedirect('/')

def basic_element(request):
    return render(request,'pages/forms/basic_elements.html')

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')