from django.shortcuts import render

# Create your views here.
from questionario.forms import QuestForm


def quest(request):
    context = {}
    context['form'] = QuestForm()

    return render(request,'quest_form.html',context)