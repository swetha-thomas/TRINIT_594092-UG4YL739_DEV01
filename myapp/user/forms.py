from django import forms
from .models import Ngo, Philanthropist
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)
    username = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class NgoRegisterForm(forms.ModelForm):
    class Meta:
        model = Ngo
        fields = ['org_name','gsn','state','certification','phone_number','primary_cause','website_url', 'description',]


class PhilanthropistRegisterForm(forms.ModelForm):
    class Meta:
        model = Philanthropist
        fields = ['org_name','primary_cause','state','phone_number']