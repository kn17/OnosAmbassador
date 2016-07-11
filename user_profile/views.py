from django.shortcuts import render_to_response, render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from forms import UserProfileForm
from events.models import Event
from reports.models import Reports
import datetime

# Create your views here.

@login_required
def update_profile(request, id=None):
    title = "Edit Profile"
    instance = get_object_or_404(UserProfile, id=id)
    form = UserProfileForm(request.POST or None,request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse("profiles:profile", args=[request.user.id]))
    return render(request, 'forms.html', {'instance': instance, 'title': title, 'form': form})


def profile(request, profile_id):
    if profile_id == "0":
        if request.user.is_authenticated:
            userProfile = UserProfile.objects.get(pk=profile_id)
    else:
        userProfile = UserProfile.objects.get(pk=profile_id)
        latest_events = Event.objects.filter(user_id=profile_id).order_by('date', 'time')
        latest_reports = Reports.objects.filter(user_id=profile_id).order_by('report_date','report_title')
        userid = userProfile.user_id
        temp = User.objects.get(id = userid)
        if request.user.is_authenticated:
            if userProfile.user_id == request.user.id or request.user.is_staff:
                allow = True
            else:
                allow =False
        else:
            allow=False
    return render_to_response('user_profile/profile.html', {'userProfile':userProfile, 'latest_events':latest_events, 'latest_reports':latest_reports, 'allow':allow, 'temp':temp}, RequestContext(request))

@login_required
def create_profile(request):
    title = "Create a new Profile"
    form = UserProfileForm(request.POST or None,request.FILES or None, initial={'name':request.user.get_full_name()})
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = User.objects.get(id=request.user.id)
        UserProfile.location = form.cleaned_data.get('city') + ', ' + form.cleaned_data.get('country')
        instance.save()
        return HttpResponseRedirect(reverse("profiles:profile", args=[request.user.id]))
    return render(request, 'forms.html', {"form":form, "title":title})