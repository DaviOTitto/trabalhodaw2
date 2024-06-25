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
class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nome
class DoacaoForm(forms.ModelForm):
    # Outros campos do formulário aqui

    codigo_doador = forms.ModelChoiceField(queryset=Doador.objects.all(), empty_label=None)

    class Meta:
        model = Doacao
        fields = ('Data', 'Hora', 'volume', 'situacao', 'codigo_doador')