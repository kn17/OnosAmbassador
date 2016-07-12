from django import forms
from models import UserProfile
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from reports.models import Reports

class UserProfileForm(forms.ModelForm):

    name = forms.CharField(max_length=100)
    bio = forms.Textarea()
    image = forms.FileField(label='Profile Photo')
    country = CountryField(blank_label='(Select Country)')
    city = forms.CharField(max_length=100)
    twitter = forms.CharField(max_length=100, required=False)
    linkedin = forms.CharField(max_length=100, required=False)
    class Meta:
        model = UserProfile
        exclude = ('user','location')



