import uuid
import re
from django.db import models
#from stdimage.models import StdImageField
from django.utils import timezone
from pathlib import Path, os
from django.db.models import signals

class Teste(models.Model):
    options_choices = (
        ('1', 'option 1 '),
        ('F', 'option 2 '),
    )
    texto = models.TextField("texto",null = True)
    interio = models.IntegerField("inteiro",blank=True)
    Boolean = models.BooleanField("booelan",blank=True,null=True)
    #lista = models.CharField("escolha", choices = options_choices)
    escolha_radio = models.IntegerField("escolharadio", null =True)


