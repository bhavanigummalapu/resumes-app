from django import forms

from .models import resumus

class EmailForm(forms.ModelForm):
  class Meta:
    model = resumus
    fields= '__all__'