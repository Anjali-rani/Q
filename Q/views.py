from django.contrib.auth.models import User
from django.shortcuts import render


def index(request):
    return render(request,'data.html')

def data(request):
    user=User.objects.create_user(last_name=request.POST['RN'],username=request.POST['AD'])
    return render(request,'data.html')