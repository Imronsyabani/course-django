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
    if request.session.get('_redirect_admin'):
        return render(request,'pages/forms/basic_elements.html')
    else:
        return HttpResponseRedirect('/')

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')

def course_form(request):
    return render(request,'pages/forms/course_form.html')

def passing_url(request):
    if request.session.get('_redirect_admin'):
        return HttpResponseRedirect('/admin')