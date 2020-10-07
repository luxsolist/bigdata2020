from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# from .forms import UserForm

# from django import forms
# from django.contrib.auth.forms import UserCreationForm


from tour.models import TourInfo

def signup(request):
    tourlist = TourInfo.objects.all()
    # if request.method == 'POST':
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         new_user = User.objects.create_user(**form.cleaned_data)
    #         login(request,new_user)
    #         return redirect('index')

    # else:
    #     form = UserForm()
    #     return render(request,'account/signup.html',{'tourlist':tourlist,'form':form})
    return render(request,'account/signup.html',{'tourlist':tourlist})

def index1(request):
    return HttpResponse('<h1>hello</h1>')