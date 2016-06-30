from django.shortcuts import render_to_response, render
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
def update_profile(request):
    userProfile = UserProfile.objects.get(user = request.user)
    form = UserProfileForm(initial={'bio':userProfile.bio, 'name':userProfile.name, 'image':userProfile.image})
    return render_to_response('user_profile/update_profile.html',{'form':form}, RequestContext(request))

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
            if userProfile.user_id == request.user.id:
                allow = True
            else:
                allow =False
        else:
            allow=False
    return render_to_response('user_profile/profile.html', {'userProfile':userProfile, 'latest_events':latest_events, 'latest_reports':latest_reports, 'allow':allow, 'temp':temp}, RequestContext(request))


@login_required
def send_update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            userProfile = UserProfile.objects.get(user=request.user)
            bio = form.cleaned_data['bio']
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']
            userProfile.name = name
            userProfile.bio = bio
            userProfile.image = image
            userProfile.save()
            return redirect('/profiles/profile/' + str(userProfile.id))
    else:
        form = UserProfileForm()

    return redirect('/profiles/send_update_profile')

@login_required
def create_profile(request):
    title = "Create a new Profile"
    form = UserProfileForm(request.POST or None,request.FILES or None, initial={'name':request.user.get_full_name()})
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = User.objects.get(id=request.user.id)
        instance.save()
        return HttpResponseRedirect(reverse("profiles:profile", args=[request.user.id]))
    return render(request, 'forms.html', {"form":form, "title":title})