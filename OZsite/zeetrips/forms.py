from django import forms

from .models import Visplek

class VisplekForm(forms.ModelForm):
    class Meta:
        model= Visplek
        fields= ["vistrip", "visser", ]

class VisplekinschrijfForm(forms.ModelForm):
    class Meta:
        model= Visplek
        fields= ["vistrip", "visser", ]
        widgets = {'vistrip': forms.HiddenInput(),'visser': forms.HiddenInput()  }