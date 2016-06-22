from django import forms
from .models import *

class UniversidadForm(forms.ModelForm):
    class Meta:
        model = Universidad
        fields = ('',)
