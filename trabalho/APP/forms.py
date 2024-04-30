from django import forms

from .models import *

#from rest_framework import serializers


class TesteForm(forms.ModelForm):
    class Meta:
         model = Teste
         fields = ('texto','interio','Boolean','lista','escolha_radio')
         widgets = {
            'Boolean': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'escolha_radio': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
         field_order = ('texto','interio','Boolean','lista','escolha_radio')
