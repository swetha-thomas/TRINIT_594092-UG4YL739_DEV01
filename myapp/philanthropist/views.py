from django.shortcuts import render
from user.models import Ngo, Philanthropist
from ngo.models import Event
from user.models import BaseUser

# Create your views here.
def philanthropistHome(request):
  philanthropist = Philanthropist.objects.get(user=request.user)
  events = Event.objects.all()
  user = request.user
  for event in events:
      event.perc = event.funds_raised/event.funds_required*100
  return render(request, 'philanthropist/philanthropist_home.html', {'events':events,
    'orgName': philanthropist.org_name, 'philanthropist':philanthropist, 'user':user
  })

def philanthropistSearch(request):
    form = dict(request.POST)
    user = request.user
    philanthropist = Philanthropist.objects.get(user=request.user)
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
    return render(request, 'philanthropist/philanthropist_search.html', {'user':user, 'orgName': philanthropist.org_name, 'ngos' : filtered_ngos})

def philanthropistCalculate(request, event_name, org_name, user_name):
    form = dict(request.POST)
    print(form)
    amount = int(form.get('amount')[0])
    user = BaseUser.objects.get(username=user_name)

    philanthropist = Philanthropist.objects.get(user=user)
    ngo = Ngo.objects.get(org_name=org_name)
    event = Event.objects.get(event_name=event_name)
    philanthropist.trust_score += (amount/50000)
    philanthropist.fund_contrib += amount
    event.funds_raised += amount
    ngo.fund_received += amount
    cert_score = {'Platinum':3, 'Gold':2, 'Silver':1}
    ngo.trust_score += (amount/50000)*cert_score[ngo.certification]
    ngo.save()
    philanthropist.save()
    event.save()
    events = Event.objects.all()
    for event in events:
      event.perc = event.funds_raised/event.funds_required*100
    return render(request, 'philanthropist/philanthropist_home.html', {'events':events,
    'orgName': philanthropist.org_name, 'philanthropist':philanthropist, 'user':user,
  })

def philanthropistLike(request, org_name):
    user = request.user
    philanthropist = Philanthropist.objects.get(user=user)
    ngo = Ngo.objects.get(org_name=org_name)
    cert_score = {'Platinum':3, 'Gold':2, 'Silver':1}
    ngo.trust_score += philanthropist.trust_score*cert_score[ngo.certification]
    ngo.save()
    print(philanthropist.trust_score)
    ngos = Ngo.objects.all()

    return render(request, 'philanthropist/philanthropist_search.html', {'user':user, 'orgName': philanthropist.org_name, 'ngos' : ngos})



