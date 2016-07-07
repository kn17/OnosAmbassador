from django import forms
from .models import Reports

class Report(forms.ModelForm):
    report_title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    activity = forms.ChoiceField(choices=Reports.ACTIVITY_CHOICES)
    activity_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


    class Meta:
        model = Reports
        fields = { 'content','report_title', 'activity','activity_date'}