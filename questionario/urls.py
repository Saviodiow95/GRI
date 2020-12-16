from django.urls import path, include

from questionario.views import quest, obrigado, rel_dif_temp

urlpatterns = [
    path('', quest, name='quest'),
    path('obrigado/', obrigado, name='obrigado'),
    path('relatorio/tempo_dificuldade/', rel_dif_temp, name='rel_dif_temp'),

]
