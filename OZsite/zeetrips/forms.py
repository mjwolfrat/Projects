from django import forms

from .models import Visplek

class VisplekForm(forms.ModelForm):
    class Meta:
        model= Visplek
        fields= ["vistrip", "visser"]
