from django import forms
from .models import Event

class Events(forms.ModelForm):
    name = forms.CharField(max_length=255)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField()
    organized_by = forms.CharField(max_length=255)
    location = forms.CharField(max_length=255)

    class Meta:
        model = Event
        fields = {'name', 'date', 'time', 'organized_by', 'location'}