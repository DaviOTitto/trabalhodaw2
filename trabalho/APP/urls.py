from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls.static import media 
from rest_framework import routers
from .views import *


urlpatterns = [
    path('',home,name="home"),
    path('conc2/',inserttest,name='formu'),
    path('conc/',teste2,name='teste2'),
    path('mar6/',mar6,name='mar6'),
    path('men6/',men6,name='men6'),
    path('Lista_Doador/',Doador_list,name='Doador_list'),
    path('Lista_Doacao/',listar_doacoes,name='Doacao_list'),
    path('formulario/',formulario,name='formulario'),
    path('adcionar_doador/',insertdoador,name='insertdoador'),
    path('<int:pk>/',view=detalhe_formulario,name='detalhe_formulario'),
    path('Doador/<int:pk>/',view=detalhe_doador,name='detalhe_doador'),
    path('deleta_Doador/<int:pk>/',view=deleta_doador,name='deleta_doador'),
    path('altera_doador/<int:pk>/',view=altera_doador,name='altera_doador'),
    path('insere_doacao/',view=insertdoacao,name='insertdoacao'),
]