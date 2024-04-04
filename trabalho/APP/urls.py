from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls.static import media 
from rest_framework import routers
from .views import *


urlpatterns = [
    path('',teste,name="teste"),
    path('conc/',inserttest,name='teste2'),
    path('mar6/',mar6,name='mar6'),
    path('men6/',men6,name='men6'),
    path('formulario/',formulario,name='formulario'),

]