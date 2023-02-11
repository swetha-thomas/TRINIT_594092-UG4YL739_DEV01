from django.shortcuts import render
from user.models import Ngo, Philanthropist
# Create your views here.
def ngoHome(request):
  ngo = Ngo.objects.get(user=request.user)
  return render(request, 'ngo/ngo_home.html', {
    'orgName': ngo.org_name
  })