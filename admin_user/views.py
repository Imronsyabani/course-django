from django.shortcuts import render
from django.views import defaults
# Create your views here.
def index(request,exception=None):
    return defaults.page_not_found(request,template_name='404.html')

def dashboard(request):
    return render(request,'dashboard.html')