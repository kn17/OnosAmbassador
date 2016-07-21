from django.shortcuts import render_to_response, render
from django.template import RequestContext
from .models import Event
from .forms import Events
from user_profile.models import UserProfile
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user.is_authenticated():
        user = UserProfile.objects.get(pk=request.user.id)
    else:
        user = None
    return render_to_response('events/event.html', {'event':event,'userProfile':user}, RequestContext(request))


def create_event(request):
    title = "Create a new Event"
    form = Events(request.POST or None, initial={'organized_by':request.user.get_full_name()})
    if request.user.is_authenticated():
        userprofile = UserProfile.objects.get(pk=request.user.id)
    else:
        userprofile = None
    if form.is_valid():
        obj = Event()
        obj.name = form.cleaned_data.get('name')
        obj.date = form.cleaned_data.get('date')
        obj.time = form.cleaned_data.get('time')
        obj.organized_by = form.cleaned_data.get('organized_by')
        obj.location = form.cleaned_data.get('location')
        obj.user_id = request.user.id
        obj.save()
        return HttpResponseRedirect(reverse("profiles:profile", args=[request.user.id]))
    return render(request, 'forms.html', {"form":form, "title":title, 'userProfile':userprofile})