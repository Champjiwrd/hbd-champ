from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required
def index(request,name):
    print('test')
    return render(request,'index.html',{'name':name})