from django.shortcuts import render_to_response
from django.template import RequestContext
from events.models import Event
from announcements.models import Announcements
from user_profile.models import UserProfile
from django.contrib.auth.models import User
import datetime
from braces import views
from django.views import generic
from .forms import LoginForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login, authenticate, logout

def home(request):
    latest_events = Event.objects.exclude(date__lt=datetime.date.today()).order_by('date','time')[:4]
    latest_announcements = Announcements.objects.order_by('-timestamp')[:4]
    context = {'latest_events':latest_events, 'latest_announcements': latest_announcements}
    return render_to_response('home.html', context, RequestContext(request))

def team(request):
    ambassador_team = UserProfile.objects.exclude(user__is_staff=1).order_by('name')
    team = UserProfile.objects.filter(user__is_staff=1).order_by('name')
    return render_to_response('team.html',{'team':team,'ambassador_team':ambassador_team}, RequestContext(request))
