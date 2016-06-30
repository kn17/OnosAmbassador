from django import forms
from models import UserProfile

class UserProfileForm(forms.ModelForm):

    name = forms.CharField(max_length=100)
    bio = forms.Textarea()
    image = forms.FileField(label='Profile Photo')
    location = forms.CharField(max_length=100)
    twitter = forms.CharField(max_length=100, required=False)
    linkedin = forms.CharField(max_length=100, required=False)
    class Meta:
        model = UserProfile
        exclude = ('user',)

