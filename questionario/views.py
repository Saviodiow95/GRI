from django.shortcuts import render

# Create your views here.
from questionario.forms import QuestForm


def quest(request):
    context = {}


    if request.method == "POST":
        form = QuestForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context['form'] = QuestForm(request.POST)
    else:
        context['form'] = QuestForm()


    return render(request,'quest_form.html',context)