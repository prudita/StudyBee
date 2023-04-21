from django import forms
from django.utils.timezone import now
from .models import StudyPlan

class StudyPlanForm(forms.ModelForm):
    class Meta:
        model = StudyPlan
        fields = ['name', 'type', 'subject', 'date', 'location', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    name = forms.CharField(
        max_length=50, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter plan name', 'class': 'form-control'})
    )

    type = forms.ChoiceField(
        choices=StudyPlan.TYPE_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    subject = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter subject', 'class': 'form-control'})
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
        initial=now()
    )

    location = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter location', 'class': 'form-control'})
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter description', 'class': 'form-control'})
    )
