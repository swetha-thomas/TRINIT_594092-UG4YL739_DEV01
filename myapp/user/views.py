from django.shortcuts import render, redirect
from .forms import NgoRegisterForm, PhilanthropistRegisterForm, SignUpForm


# Create your views here.

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