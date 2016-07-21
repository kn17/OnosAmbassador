from django.shortcuts import render_to_response
from django.template import RequestContext
from events.models import Event
from announcements.models import Announcements
from user_profile.models import UserProfile, Mentor
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test
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

def contact(request):
    if request.user.is_authenticated():
        user = UserProfile.objects.get(pk=request.user.id)
    else:
        user = None
    return render_to_response('contact_us.html',{'userProfile':user,}, RequestContext(request))

def contact_logic(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    message = request.GET.get('message')
    cc_myself = request.GET.get('cc_myself')
    subject = "New Message from " + first_name + " " + last_name
    recipients = ['ambassadors@onlab.us']
    if cc_myself:
        recipients.append(email)

    send_mail(subject, message, email, recipients)
    return HttpResponseRedirect(reverse('home'))

@user_passes_test(lambda u: u.is_staff)
def dashboard(request):
    events_count = Event.objects.all().count()
    if request.user.is_authenticated():
        user = UserProfile.objects.get(pk=request.user.id)
    else:
        user = None
    mentors = User.objects.filter(is_staff=True).values_list('first_name', 'last_name')
    print mentors
    mentor={}
    for x in mentors:
        name = x[0] + ' ' + x[1]
        mentor[name]=Mentor.objects.filter(mentor__name__icontains=name).values_list('mentee__name', flat=True)
    print mentor
    return render_to_response('dashboard.html',{'events_count':events_count,'userProfile':user,'mentor':mentor}, RequestContext(request))