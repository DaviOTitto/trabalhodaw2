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
    CHOICES = (
        ('1', 'Opção 1'),
        ('2', 'Opção 2'),
        ('3', 'Opção 3'),
        ('4', 'Opção 4'),
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
    Boolean = models.BooleanField("booelan", blank=True, null=True,default=False)
    lista = models.CharField("escolha", choices=options_choices)
    escolha_radio = models.CharField("escolharadio", null=False, choices = CHOICES)
     
    
    def get_detalhe(self):
        return f'/teste/{self.id}'


class Doador(models.Model):
    options_choices = (
        ('A', ' tipo A  '),
        ('B', 'tipo  B  '),
        ('AB','tibo AB  '),
        ('O', 'tipo  O  '),        
    )
    CHOICES = (
        ('+', 'RH +   '),
        ('-', 'RH -   '),
    )
    codigo = models.AutoField("alto completo",null=False,primary_key=True)
    nome = models.CharField("Nome",blank=True,max_length=200)
    cpf = models.CharField("CPF",blank=True,max_length=11)
    contato = models.CharField("numero",blank=True,max_length=12)
    tipo_sanguineo = models.CharField("tipo sanguineo",blank=True,null =False ,max_length=4 ,choices = options_choices)
    rh = models.CharField("RH",blank=True,max_length=1 ,choices= CHOICES)
    tipo_rh_corretos = models.BooleanField("RH corretos",blank=True)
    situacao = models.CharField("situcao", blank=True)
    class Meta:
        ordering = ['codigo']
        verbose_name = 'Doador'
    def get_detalhe(self):
        return f'/teste/Doador/{self.codigo}/'
    def get_modifica(self):
        return f'/teste/altera_doador/{self.codigo}/'
    def get_exclui(self):
        return f'/teste/deleta_Doador/{self.codigo}/'

class Doacao(models.Model):
    codigo = models.AutoField("alto completo",null=False,primary_key=True)
    Data = models.DateField("Data",blank=True,null=False)
    Hora = models.TimeField("time",blank=True,null=False)
    volume = models.DecimalField("volume",decimal_places = 2 , max_digits = 7)
    situacao = models.CharField("situcao", blank=True)
    codigo_doador = models.ForeignKey(Doador,db_column='codigo_doador',related_name='codigo_do',on_delete=models.CASCADE)  
    class Meta:
        ordering = ['codigo']
        verbose_name = 'Doador'
        verbose_name_plural = 'Doadores'



