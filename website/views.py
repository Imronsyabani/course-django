from django.http import request,HttpResponseRedirect
from django.shortcuts import render

def index(request):
    if request.session.get('_redirect_admin'):
        return HttpResponseRedirect('/admin')
    return render(request,'index.html')