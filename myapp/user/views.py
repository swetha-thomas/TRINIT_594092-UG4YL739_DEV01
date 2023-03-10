from django.shortcuts import render, redirect
from .forms import NgoRegisterForm, PhilanthropistRegisterForm, SignUpForm
from django.contrib.auth import authenticate, login as login_user
from user.models import Philanthropist, Ngo

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect

import requests
from bs4 import BeautifulSoup

# Create your views here.

def emailExtractor(urlString):
  emails = []
  getH = requests.get(urlString)
  h=getH.content
  soup = BeautifulSoup(h,'html.parser')
  a_tags = soup.find_all('a',href=True)

  for atag in a_tags:
    if "mailto:" in atag['href']:
      emails.append(atag.text)
  
  return emails

def landing_page_view(request):
    return render(request, 'user/landing_page.html')

def register(request, user_type):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        d_form = (NgoRegisterForm(request.POST) if
                  user_type == 'ngo' else PhilanthropistRegisterForm(request.POST))
        if form.is_valid() and d_form.is_valid():
            user = form.save(commit=False)
            user.is_ngo = True if user_type == 'ngo' else False
            user.is_philanthropist = True if user_type == 'philanthropist' else False

            if user_type=='ngo':
              gsn = str(d_form.cleaned_data['gsn'])
              email = form.cleaned_data['email']
              emailList = []
              htmlString = 'https://guidestarindia.org/summary.aspx?CCReg='
              urlString = htmlString+gsn
              emailList=emailExtractor(urlString)

              if emailList[0]==email:    
                user.save()
                d_form = d_form.save(commit=False)
                d_form.user = user
                d_form.save()
                return redirect('login')
              else:
                return redirect('/register/ngo')
            else:
              user.save()
              d_form = d_form.save(commit=False)
              d_form.user = user
              d_form.save()
              return redirect('login')
    else:
        form = SignUpForm()
        d_form = NgoRegisterForm() if user_type == 'ngo' else PhilanthropistRegisterForm()
    context = {
        'form': form,
        'd_form': d_form,
        'user_type': user_type
    }
    return render(request, 'user/register.html', context)

def login(request):
  if request.method == 'POST':
    if request.POST.get('user_type') == 'ngo':
      password = request.POST["password"]
      username = request.POST["username"]
      user = authenticate(username=username, password=password)
      if user is not None:
        login_user(request, user)
        
        if Ngo.objects.filter(user=user).count() != 0:
          return redirect('ngoHome')
        else:
          messages.info(request, "NGO Doesnt Exist")
          return redirect('login')
      else:
        messages.info(request, "Invalid Credentials")
        return redirect('login')
    else:
      # email = request.POST["email"]
      password = request.POST["password"]
      username = request.POST["username"]
      user = authenticate(username=username, password=password)
      if user is not None:
        login_user(request, user)
        
        if Philanthropist.objects.filter(user=user).count() != 0:
          return redirect('philanthropistHome')
        else:
          messages.info(request, "Philanthropist Doesnt Exist")
          return redirect('login')
      else:
        messages.info(request, "Invalid Credentials")
        return redirect('login')
    
  return render(request, 'user/login.html')

def logout(request):
  # logout user and finish up all loose ends
  auth.logout(request)
  return redirect('login')