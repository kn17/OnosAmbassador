from django.shortcuts import render, get_object_or_404
from .models import Announcements

# Create your views here.
def announcement_detail(request, announcement_id):
    ann = get_object_or_404(Announcements,pk=announcement_id)
    return render(request,'announcements.html',{'announcement':ann})