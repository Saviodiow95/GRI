from django.urls import path, include

from questionario.views import quest, obrigado, rel_dif_temp, rel_geral, QuestlList, quest_delete, quest_edit

urlpatterns = [
    path('', quest, name='quest'),
    path('list/', QuestlList.as_view(), name='quest_list'),
    path('delete/<int:id>', quest_delete, name='quest_delete'),
    path('edit/<int:id>', quest_edit, name='quest_edit'),

    path('obrigado/', obrigado, name='obrigado'),
    path('relatorio/geral/', rel_geral, name='rel_geral'),
    path('relatorio/tempo_dificuldade/', rel_dif_temp, name='rel_dif_temp'),

]
