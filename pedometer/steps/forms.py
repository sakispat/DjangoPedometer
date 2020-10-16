from django import forms
from django.forms import ModelForm
from .models import Step


class StepForms(forms.ModelForm):
	steps = forms.IntegerField(label='Steps', widget=forms.TextInput(attrs={'class': 'form-control'}))
	days = forms.DateField(label='Days', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

	class Meta:
	    model = Step
	    fields = ('steps', 'days')
