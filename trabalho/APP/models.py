import uuid
import re

#from stdimage.models import StdImageField
from django.utils import timezone
from pathlib import Path, os
from django.db.models import signals
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator,MinValueValidator,MaxValueValidator

class Teste(models.Model):
    options_choices = (
        ('1', 'option 1 '),
        ('F', 'option 2 '),
    )
    id = models.AutoField("id",primary_key=True, null=False)
    texto = models.TextField("texto", null=True, max_length=255, validators=[
        MinLengthValidator(2, "O texto deve ter no mínimo 2 caracteres."),
        MaxLengthValidator(255, "O texto deve ter no máximo 255 caracteres.")
    ])
    interio = models.IntegerField("inteiro", blank=True, validators=[
      MinValueValidator(1, "O valor inteiro deve ser maior que 0."),
      MaxValueValidator(1000, "O valor inteiro não pode exceder 1000.")
    ])
    Boolean = models.BooleanField("booelan", blank=True, null=True)
    lista = models.CharField("escolha", choices=options_choices)
    escolha_radio = models.CharField("escolharadio", null=False, max_length=30)
     
    
    def get_detalhe(self):
        return f'/teste/{self.id}'


class Doador(models.Model):
    codigo = models.AutoField("alto completo",null=False,primary_key=True)
    nome = models.CharField("Nome",blank=True,max_length=200)
    cpf = models.CharField("CPF",blank=True,max_length=11)
    contato = models.CharField("numero",blank=True,max_length=12)
    tipo_sanguineo = models.CharField("tipo sanguineo",blank=True,max_length=4)
    rh = models.CharField("RH",blank=True,max_length=1)
    tipo_rh_corretos = models.BooleanField("RH corretos",blank=True)
    situacao = models.CharField("situcao", blank=True)
    class Meta:
        ordering = ['codigo']
        verbose_name = 'Doador'
class Doacao(models.Model):
    codigo = models.AutoField("alto completo",null=False,primary_key=True)
    Data = models.DateField("Data",auto_now_add=True,auto_now=False)
    Hora = models.TimeField("time",auto_now_add=True,auto_now=False)
    volume = models.DecimalField("volume",decimal_places = 2 , max_digits = 7)
    situacao = models.CharField("situcao", blank=True)
    codigo_doador = models.ForeignKey(Doador,db_column='codigo_doador',related_name='codigo_do',on_delete=models.CASCADE)  
    class Meta:
        ordering = ['codigo']
        verbose_name = 'Doador'



