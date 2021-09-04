from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    context = {
            "su": User.objects.filter(is_superuser=True).values_list('username')
        }
    return render(request,'user/home.html', context)
    
def login(request):
    return render(request, 'user/login.html')