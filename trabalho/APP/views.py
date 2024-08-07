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
from dateutil.parser import parse 
from datetime import timedelta

home = TemplateView.as_view(template_name='index.html')


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
        forms.instance.situacao = 'ativo'
        teste_instance = forms.save()        
        return HttpResponseRedirect(resolve_url('detalhe_doador',teste_instance.pk))
    else:
        forms = DoadorForm(instance=order_forms, prefix='main')
        
    context = {
        'forms': forms,
      }
    return render(request,'novo_doador.html',context)        
        

def insertdoacao(request):
    doadores = Doador.objects.all()

    # Crie uma lista de tuplas (código, nome) para usar no campo de escolha
   

    order_forms = Doacao()
    if request.method == 'POST':
      forms = DoacaoForm(request.POST, request.FILES,
                          instance=order_forms, prefix='main')
      #codigo =  int(request.POST.get("id_main-codigo_doador"))
      #doador = Doador.objects.get(pk=codigo)

    # Modifique o campo tipo_rh_corretos
      #doador.tipo_rh_corretos = True
     # doador.save()         
      if forms.is_valid() :
        teste_instance = forms.save()
      #  return HttpResponseRedirect(resolve_url('detalhe_doador',teste_instance.pk))
    else:
        forms = DoacaoForm(instance=order_forms, prefix='main')
        
    context = {
        'forms': forms,
      }
    return render(request,'insere_doacao.html',context)        
         


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
    i = 1
    if request.method == 'GET':
        forms = DoadorForm(instance=doador,prefix='main')
    else:
        forms = DoadorForm(request.POST,request.FILES,instance=doador,prefix='main')
        if forms.is_valid():
            forms = forms.save(commit=False)
            # apagado user.profile da linha 163 , Davi Oliveira Tito 02/05/2022
            i = 0     
            forms.save()
            return HttpResponseRedirect(resolve_url('detalhe_doador',forms.pk))
        else:
            print("erro no doador")
    context = {
        'forms':forms,
    }
    return render(request,'altera_doador.html',context)

def deleta_doador(request,pk):
    print("entrou ")
    doador = get_object_or_404(Doador,pk=pk)
    doador.situacao = 'inativo'
    doador.save() 
    return redirect('Doador_list')

def listar_doacoes(request):
    object_list = Doacao.objects.all().order_by('-codigo')

    # filtro na lista por datas
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    print(data_inicial)
    print(data_final)
    if data_inicial and data_final:
        data_final = parse(data_final) + timedelta(1)
        object_list = object_list.filter(Data__range=[data_inicial, data_final])

    # pesquisa na lista de vendas pelo nome do cliente        
    search = request.GET.get('search_box')
    if search:
        object_list = object_list.filter(codigo_doador__nome__icontains=search)

    # retorna as vendas do cliente, vindo da página de customers
   # if 'cadastros_sale' in request.GET:
    #    object_list = object_list.filter(codigo_doador=request.GET['cadastros_sale'])

    # retorna as vendas do usuário, vindo da página de usuários
    #if 'usuario_sale' in request.GET:
      #  object_list = object_list.filter(usuario_ven=request.GET['usuario_sale'])

    # retorna as vendas do setor, vindo da página de setor    
   #if 'setor_sale' in request.GET:
      #  object_list = object_list.filter(setor_ven=request.GET['setor_sale'])

    paginator = Paginator(object_list, 20)
    page = request.GET.get('page', 1)
    try:
        vendas = paginator.page(page)
    except PageNotAnInteger:
        vendas = paginator.page(1)
    except EmptyPage:
        vendas = paginator.page(paginator.num_pages)

    context = {'object_list':object_list}
    return render(request,'lista_doacoes.html',context)
  
def Doador_list(request):
    # Obtém todos os objetos da tabela Doador
    object_list = Doador.objects.all().order_by('codigo')

    # Instancia o formulário com os dados da requisição GET
    form = DoadorForm(request.GET)

    # Verifica se o formulário é válido
    if form.is_valid():
        # Obtém os dados do formulário
        nome = form.cleaned_data.get('nome')
        cpf = form.cleaned_data.get('cpf')
        contato = form.cleaned_data.get('contato')
        tipo_sanguineo = form.cleaned_data.get('tipo_sanguineo')
        rh = form.cleaned_data.get('rh')
        tipo_rh_corretos = form.cleaned_data.get('tipo_rh_corretos')
        situacao = form.cleaned_data.get('situacao')

        # Aplica os filtros conforme necessário
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
            object_list = object_list.filter(tipo_rh_corretos__exact=tipo_rh_corretos)
        if situacao:
            object_list = object_list.filter(situacao__icontains=situacao)

    # Paginação dos resultados
    paginator = Paginator(object_list, 20)
    page = request.GET.get('page', 1)
    try:
        doador = paginator.page(page)
    except PageNotAnInteger:
        doador = paginator.page(1)
    except EmptyPage:
        doador = paginator.page(paginator.num_pages)

    context = {
        'object_list': object_list,
        'doador': doador,
        'form': form
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
