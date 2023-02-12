from django.shortcuts import render
from user.models import Ngo, Philanthropist
from .models import Event
# Create your views here.
def ngoHome(request):
  ngo = Ngo.objects.get(user=request.user)
  user = request.user
  events = Event.objects.all()
  print(events)
  return render(request, 'ngo/ngo_home.html', { 'ngo':ngo, 'user':user,
    'orgName': ngo.org_name, 'events':events
  })

def ngoSearch(request):
    user = request.user
    form = dict(request.POST)
    ngo = Ngo.objects.get(user=request.user)
    primary_cause = form.get('primary_cause')
    state = form.get('state')
    certification = form.get('certification')
    trust_score = form.get('trust_score')
    ngos = Ngo.objects.all()
    states = ['Andhra Pradesh', 'Karnataka', 'Kerala', 'Maharashtra', 'Rajasthan', 'Tamil Nadu']
    filtered_ngos = set({})
    for ngo in Ngo.objects.all():

        if ((primary_cause is None or ((set(list(ngo.primary_cause)) & set(primary_cause)) == set(primary_cause))) and (state is None or ngo.state in state) and (certification is None or ngo.certification in certification) and (trust_score is None or ngo.trust_score>trust_score)):
            filtered_ngos.add(ngo)
    print(filtered_ngos)
    return render(request, 'ngo/ngo_search.html', {'user':user, 'orgName':ngo.org_name, 'ngos' : filtered_ngos, 'states' : states})

def ngoEvent(request):

  if(request.method == 'POST'):
    
    event_name = request.POST['event_name']
    event_description = request.POST['event_description']
    funds_required = request.POST['funds_required']
    date = request.POST['date']

    event = Event.objects.create(
      event_name = event_name,
      ngo = Ngo.objects.get(user=request.user),
      event_description = event_description,
      funds_required = funds_required,
      date = date,
    )
    event.save()
    # form = dict(request.POST)
    # print(form)
  ngo=Ngo.objects.get(user=request.user)
  events=Event.objects.all().filter(ngo=Ngo.objects.get(user=request.user))
  return render(request, 'ngo/ngo_events.html', {'ngo':ngo, 'orgName':ngo.org_name, 'events':events, 'role':'create', 'user':request.user})

