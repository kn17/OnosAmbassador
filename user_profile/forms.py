from django import forms
from models import UserProfile, Mentor
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
        exclude = ('user',)

class MentorForm(forms.ModelForm):
    mentor_choices = tuple(UserProfile.objects.filter(user__is_staff=1).order_by('name').values_list('name', 'name'))
    mentee_choices = tuple(UserProfile.objects.exclude(user__is_staff=1).order_by('name').values_list('name', 'name'))
    mentor_name = forms.ChoiceField(choices=mentor_choices)
    mentee_name = forms.ChoiceField(choices=mentee_choices)

    def save(self, commit=True):
        mentor_name = self.cleaned_data.get('mentor_name', None)
        mentor_name = self.cleaned_data.get('mentee_name', None)
        return super(MentorForm, self).save(commit=commit)

    class Meta:
        model = Mentor
        fields= ('mentor_name', 'mentee_name')
