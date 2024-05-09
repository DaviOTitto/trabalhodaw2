from django.shortcuts import render, resolve_url, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator
from pathlib import Path, os
from django.views.generic import TemplateView
from .forms import *
from .models import * n

def inserttest(request):
    order_forms = Teste()
    if request.method == 'POST':
      forms = TesteForm(request.POST, request.FILES,
                          instance=order_forms, prefix='main')      
  #   ESCOLHA = request.POST.get("opcaoRadio",False)
  #   print(ESCOLHA)    
  #   order_forms.escolha_radio =str(ESCOLHA)
  #   print(order_forms.escolha_radio)      
      if forms.is_valid() :
        teste_instance = forms.save()
        return HttpResponseRedirect(resolve_url('detalhe_formulario',teste_instance.pk))
    else:
        forms = TesteForm(instance=order_forms, prefix='main')
        
    context = {
        'forms': forms,
      }
    return render(request,'teste2.html',context)
def insertdoador(request):
    order_forms = Doador()
    if request.method == 'POST':
      forms = DoadorForm(request.POST, request.FILES,
                          instance=order_forms, prefix='main')      
  #   ESCOLHA = request.POST.get("opcaoRadio",False)
  #   print(ESCOLHA)    
  #   order_forms.escolha_radio =str(ESCOLHA)
  #   print(order_forms.escolha_radio)      
      if forms.is_valid() :
        teste_instance = forms.save()
        return HttpResponseRedirect(resolve_url('detalhe_formulario',teste_instance.pk))
    else:
        forms = TesteForm(instance=order_forms, prefix='main')
        
    context = {
        'forms': forms,
      }
    return render(request,'novo_doador.html',context)        
         

def teste(request):
    numero = int(request.GET.get("numero",False))
    numero2 = int(request.GET.get("numero2",False))
    print(numero)
    print (numero2) 
    numerot = numero+numero2
    if numerot > 6  :
      print('numero maior que 6 ')
    else :
      if numerot != None:
        print('numero menor que 6') 
    return render(request,'teste.html')
mar6 = TemplateView.as_view(template_name='resultado>6.html')
men6 = TemplateView.as_view(template_name='resultado<6.html')


def formulario(request):
  if request.method == 'post':  
    booelan = request.POST.get("boolean",False)
    print(boolean)
    texto = request.POST.get("testo",False)
    print(texto)
    numero = int(request.POST.get("numero",False))
    print(numero)
    string = request.POST.get("list",False)
    print(string)
    var = request.Post.get("radio",False)
    print(var)
    str(boolean +"texto "+ texto +  "numero "+ numero + "lista " + string + "radio" + var +"  fim")
    print(str)
  return render(request,'formulario.html')
def detalhe_formulario(request, pk):
    object = get_object_or_404(Teste,pk=pk)
    context = {
        'object':object,
    }
    return render(request,'detalhe_formulario.html',context)



def teste2(request):
  numero = int(request.POST.get('numero',False))
  numero2 = int(request.POST.get('numero2',False))
  print(numero)
  print (numero2)
  valor = numero+numero2
  if valor > 6 :
    return HttpResponseRedirect(resolve_url('mar6'))
      
  else :
    if valor != None:
     return HttpResponseRedirect(resolve_url('men6'))
