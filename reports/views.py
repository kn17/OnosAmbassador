from django.shortcuts import render, get_object_or_404, redirect
from .forms import Report
from user_profile.models import UserProfile
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .models import Reports

# Create your views here.

@login_required
def create_report(request):
    title = "Create a new Report"
    form = Report(request.POST or None)
    if request.user.is_authenticated():
        userprofile = UserProfile.objects.get(pk=request.user.id)
    else:
        userprofile = None
    if form.is_valid():
        obj = Reports()
        obj.report_title = form.cleaned_data.get('report_title')
        obj.content = form.cleaned_data.get('content')
        obj.activity = form.cleaned_data.get('activity')
        obj.activity_date = form.cleaned_data.get('activity_date')
        obj.created_by = request.user.username
        obj.user_id = request.user.id
        obj.save()
        return HttpResponseRedirect(reverse("profiles:profile", args=[request.user.id]))
    return render(request, 'forms.html', {"form":form, "title":title,'userProfile':userprofile})


@login_required
def edit_report(request, id=None):
    title = 'Edit Report'
    instance = get_object_or_404(Reports, id=id)
    form = Report(request.POST or None, instance = instance)
    if request.user.is_authenticated():
        userprofile = UserProfile.objects.get(pk=request.user.id)
    else:
        userprofile = None
    if  form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        return HttpResponseRedirect(reverse("profiles:profile", args=[request.user.id]))
    return render(request, 'forms.html', {'instance':instance, 'title':title, 'form':form,'userProfile':userprofile})

@login_required
def delete_report(request, id=None):
    instance = get_object_or_404(Reports, id=id)
    instance.delete()
    return redirect(reverse("profiles:profile", args=[request.user.id]))

def reports(request, id=None):
    instance = get_object_or_404(Reports, id=id)
    if request.user.is_authenticated():
        userprofile = UserProfile.objects.get(pk=request.user.id)
    else:
        userprofile = None
    return render(request, 'reports.html', {'instance':instance, 'title':instance.report_title,'userProfile':userprofile})