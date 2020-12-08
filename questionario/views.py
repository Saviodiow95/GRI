from django.shortcuts import render, redirect

# Create your views here.
from questionario.forms import QuestForm



def obrigado(request):
    return render(request,'obrigado.html')


def quest(request):
    context = {}


    if request.method == "POST":
        form = QuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('obrigado')
        else:
            context['form'] = QuestForm(request.POST)
    else:
        context['form'] = QuestForm()


    return render(request,'quest_form.html',context)