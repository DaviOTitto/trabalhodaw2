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
class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = ('nome', 'cpf', 'contato', 'tipo_sanguineo', 'rh', 'tipo_rh_corretos', 'situacao')
        widgets = {
            'tipo_rh_corretos': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tipo_sanguineo': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'rh': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
    # Correção: field_order deve estar fora da classe Meta
    field_order = ('nome', 'cpf', 'contato', 'tipo_sanguineo', 'rh', 'tipo_rh_corretos', 'situacao')
class DoacaoForm(forms.ModelForm):
    # Crie uma variável para armazenar o queryset e o rótulo vazio
    

    class Meta:
        doador_choices = forms.ModelChoiceField(queryset=Doador.objects.all(), empty_label=None)
        model = Doacao
        fields = ('Data', 'Hora', 'volume', 'situacao', 'codigo_doador')
        widgets = {
            'codigo_doador': doador_choices,  # Use a variável aqui
        }