from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .resources import ExcelResource
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
            
            temp =form.save(commit=False)
            
            temp.first_name= request.user.first_name
            temp.last_name = request.user.last_name
            temp.save()
            return redirect('export')
            
        else:
            form = forms.ExcelForm(request.POST)

    return render(request, 'accounts/home.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('registration/login.html')



def export(request):
    fileResource = ExcelResource()
    dataset = fileResource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'
    return response
