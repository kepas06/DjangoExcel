from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from . import forms


def signup(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = forms.SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    form = forms.ExcelForm(request.POST or None)
    if request.method =='POST':
        if form.is_valid():
            print('d3')
            temp =form.save(commit=False)
            print('d4')
            temp.first_name= request.user.first_name
            temp.last_name = request.user.last_name
            temp.save()
            print('d5')
            
        else:
            form = forms.ExcelForm(request.POST)

    return render(request, 'accounts/home.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
