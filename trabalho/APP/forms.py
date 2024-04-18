from django import forms

from .models import *

#from rest_framework import serializers


class TesteForm(forms.ModelForm):
    class Meta:
        fields = ('produto_ite_aux_cod','produto_ite_aux_nome','produto_ite_aux_quant','produto_ite_aux_valor')

        field_order = ('produto_ite_aux_cod','produto_ite_aux_nome','produto_ite_aux_valor','produto_ite_aux_quant')
