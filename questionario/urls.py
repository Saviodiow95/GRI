from django.urls import path, include

from questionario.views import quest, obrigado

urlpatterns = [
    path('', quest, name='quest'),
    path('obrigado/', obrigado, name='obrigado'),
]
