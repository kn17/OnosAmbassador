from django.shortcuts import render_to_response
from django.template import RequestContext
from events.models import Event
from announcements.models import Announcements
from user_profile.models import UserProfile
from django.db.models import Q
import datetime


def home(request):
    latest_events = Event.objects.exclude(date__lt=datetime.date.today()).order_by('date','time')[:4]
    latest_announcements = Announcements.objects.order_by('-timestamp')[:4]
    if request.user.is_authenticated():
        user = UserProfile.objects.get(pk=request.user.id)
    else:
        user = None
    if latest_events:
        events_user = UserProfile.objects.get(pk=latest_events[0].user.id)
    context = {'latest_events':latest_events, 'latest_announcements': latest_announcements, 'userProfile':user, 'events_user':events_user}
    return render_to_response('home.html', context, RequestContext(request))


def team(request):
    ambassador_team = UserProfile.objects.exclude(user__is_staff=1).order_by('name')
    team = UserProfile.objects.filter(user__is_staff=1).order_by('name')
    querylist_list = UserProfile.objects.all()
    query = request.GET.get("q")
    query_list =None
    if request.user.is_authenticated():
        user = UserProfile.objects.get(pk=request.user.id)
    else:
        user = None
    if query:
        query_list=querylist_list.filter(Q(name__icontains=query) |
                                         Q(location__icontains=query)
                                         )
    return render_to_response('team.html', {'team':team, 'ambassador_team':ambassador_team, 'query_list':query_list, 'userProfile':user,'query':query}, RequestContext(request))

def support_material(request):
    if request.user.is_authenticated():
        user = UserProfile.objects.get(pk=request.user.id)
    else:
        user = None
    return render_to_response('support_material.html',{'userProfile':user,}, RequestContext(request))

def about(request):
    if request.user.is_authenticated():
        user = UserProfile.objects.get(pk=request.user.id)
    else:
        user = None
    return render_to_response('about_us.html',{'userProfile':user,}, RequestContext(request))
