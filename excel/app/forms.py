from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import ExcelFile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ExcelForm(ModelForm):
    class Meta:
        model = ExcelFile
        widgets = {'first_name': forms.HiddenInput()},
        {'second_name': forms.HiddenInput()}

        fields = ['first_name','last_name','date','dateIn','dateOut','rs_back','couriers','rs','wood','eur_s','eur_ns']