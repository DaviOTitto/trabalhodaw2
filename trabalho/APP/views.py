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
from .models import * 

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
      if forms.is_valid() :
        teste_instance = forms.save()
        return HttpResponseRedirect(resolve_url('detalhe_doador',teste_instance.pk))
    else:
        forms = DoadorForm(instance=order_forms, prefix='main')
        
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

def altera_doador(request,pk):
    order_forms = Doador()
    doador = get_object_or_404(Doador,pk=pk)                        
    doador =  Doador.objects.all().order_by('pk')                   
    i = 1
    if request.method == 'GET':
        forms = DoadorForm(instance=doador,prefix='main')
    else:
        forms = DoadorForm(request.POST,request.FILES,instance=venda,prefix='main')
        if forms.is_valid() and formset.is_valid():
            forms = forms.save(commit=False)
            # apagado user.profile da linha 163 , Davi Oliveira Tito 02/05/2022
            i = 0
            for inline_form in formset:
                inline_form = inline_form.save(commit=False)
                i += 1
            forms.save()
            formset.save()
            return HttpResponseRedirect(resolve_url('core:detalhe_doador',forms.pk))
        else:
            messages.warning(request,'Erro interno ao alterar a Doador!')
    context = {
        'forms':forms,
    }
    return render(request,'core/venda/altera_doador.html',context)

def deleta_doador(request,pk):
    get_object_or_404(Doador,pk=pk).delete()
    return redirect('core:listar_vendas')
  

def Doador_list(request):
    # Obtém todos os objetos do modelo Doador 
    object_list = Doador.objects.all().order_by('codigo')
    doador_Ver = Doador()
    forms = None  # Defina a variável fora do bloco condicional

    if request.method == 'POST':
        forms = DoadorForm(request.POST, request.FILES,
                       instance=doador_Ver, prefix='main')
    # Processa a pesquisa (se houver)
    nome = request.GET.get('nome')
    cpf = request.GET.get('cpf')
    contato = request.GET.get('contato')
    tipo_sanguineo = request.GET.get('tipo_sanguineo')
    rh = request.GET.get('rh')
    tipo_rh_corretos = request.GET.get('tipo_rh_corretos')
    situacao = request.GET.get('situacao')

    if nome:
        object_list = object_list.filter(nome__icontains=nome)
    if cpf:
        object_list = object_list.filter(cpf__icontains=cpf)
    if contato:
        object_list = object_list.filter(contato__icontains=contato)
    if tipo_sanguineo:
        object_list = object_list.filter(tipo_sanguineo__icontains=tipo_sanguineo)
    if rh:
        object_list = object_list.filter(rh__icontains=rh)
    if tipo_rh_corretos:
        object_list = object_list.filter(tipo_rh_corretos__icontains=tipo_rh_corretos)
    if situacao:
        object_list = object_list.filter(situacao__icontains=situacao)

    # Configura a paginação
    paginator = Paginator(object_list, 20)
    page = request.GET.get('page', 1)
    try:
        doador = paginator.page(page)
    except PageNotAnInteger:
        doador = paginator.page(1)
    except EmptyPage:
        doador = paginator.page(paginator.num_pages)

    context = {
        'forms' : forms,
        'object_list': object_list,
        'doador': doador,
        'nome': nome,
        'cpf': cpf,
        'contato': contato,
        'tipo_sanguineo': tipo_sanguineo,
        'rh': rh,
        'tipo_rh_corretos': tipo_rh_corretos,
        'situacao': situacao,
    }

    return render(request, 'lista_doador.html', context)

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
def detalhe_doador(request, pk):
    object = get_object_or_404(Doador,pk=pk)
    context = {
        'object':object,
    }
    return render(request,'detalhe_doador.html',context)
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
