from django import forms
from .models import Ngo, Philanthropist
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    username = forms.CharField(max_length=30, required=True, help_text='Required. Enter a valid username.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class NgoRegisterForm(forms.ModelForm):
    class Meta:
        model = Ngo
        fields = ['org_name','gsn','state','certification','phone_number',]


class PhilanthropistRegisterForm(forms.ModelForm):
    class Meta:
        model = Philanthropist
        fields = ['name','org_name','phone_number']