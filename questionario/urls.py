from django.urls import path, include

from questionario.views import quest

urlpatterns = [
    path('', quest, name='quest'),
]
