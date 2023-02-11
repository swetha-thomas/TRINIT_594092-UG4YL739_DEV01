from django.shortcuts import render
from user.models import Ngo, Philanthropist

# Create your views here.
def ngoHome(request):
  ngo = Ngo.objects.get(user=request.user)
  return render(request, 'ngo/ngo_home.html', {
    'orgName': ngo.org_name
  })

def ngoSearch(request):
    form = dict(request.POST)
    primary_cause = form.get('primary_cause')
    state = form.get('state')
    certification = form.get('certification')
    trust_score = form.get('trust_score')
    ngos = Ngo.objects.all()

    filtered_ngos = set({})
    for ngo in Ngo.objects.all():

        if ((primary_cause is None or ((set(list(ngo.primary_cause)) & set(primary_cause)) == set(primary_cause))) and (state is None or ngo.state in state) and (certification is None or ngo.certification in certification) and (trust_score is None or ngo.trust_score>trust_score)):
            filtered_ngos.add(ngo)
    print(filtered_ngos)
    return render(request, 'ngo/ngo_search.html', {'ngos' : filtered_ngos})
