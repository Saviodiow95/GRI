from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView

from questionario.forms import QuestForm
from questionario.models import Quest




class QuestlList(ListView):
    template_name = 'list_quest.html'
    model = Quest

def quest_delete(request, id):
    quest = get_object_or_404(Quest,id=id)
    quest.delete()

    return redirect('quest_list')

def quest_edit(request, id):
    context ={}
    quest = get_object_or_404(Quest, id=id)

    if request.method == 'POST':
        form = QuestForm(request.POST or None, request.FILES or None, instance=quest, prefix='quest')

        if form.is_valid():
            form.save()

            return redirect('quest_list')
        else:
            context['form'] = QuestForm(request.POST or None, request.FILES or None, instance=quest, prefix='quest')


    else:
        context['form'] = QuestForm(instance=quest, prefix='quest')

    return render(request, 'edit_quest.html', context)

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




def rel_geral(request):
    context ={}
    quests = list(Quest.objects.all())
    superior = list(Quest.objects.filter(grau='1'))
    tecnico = list(Quest.objects.filter(grau='2'))

    context['quests'] = quests
    context['superior'] = superior
    context['tecnico'] = tecnico


    return render(request,'rel_geral.html',context)




def rel_dif_temp(request):
    context={}

    quests = list(Quest.objects.all())

    list_1hora       = [0, 0, 0, 0, 0]
    list_2horas      = [0, 0, 0, 0, 0]
    list_3horas      = [0, 0, 0, 0, 0]
    list_4horas      = [0, 0, 0, 0, 0]
    list_4horas_mais = [0, 0, 0, 0, 0]

    for q in quests:
        if q.pergunta8 == '1':

            if q.pergunta7 == '1':
                list_1hora[0] += 1
            if q.pergunta7 == '2':
                list_1hora[1] += 1
            if q.pergunta7 == '3':
                list_1hora[2] += 1
            if q.pergunta7 == '4':
                list_1hora[3] += 1
            if q.pergunta7 == '5':
                list_1hora[4] += 1


        elif q.pergunta8 == '2':

            if q.pergunta7 == '1':
                list_2horas[0] += 1
            if q.pergunta7 == '2':
                list_2horas[1] += 1
            if q.pergunta7 == '3':
                list_2horas[2] += 1
            if q.pergunta7 == '4':
                list_2horas[3] += 1
            if q.pergunta7 == '5':
                list_2horas[4] += 1

        elif q.pergunta8 == '3':

            if q.pergunta7 == '1':
                list_3horas[0] += 1
            if q.pergunta7 == '2':
                list_3horas[1] += 1
            if q.pergunta7 == '3':
                list_3horas[2] += 1
            if q.pergunta7 == '4':
                list_3horas[3] += 1
            if q.pergunta7 == '5':
                list_3horas[4] += 1

        elif q.pergunta8 == '4':

            if q.pergunta7 == '1':
                list_4horas[0] += 1
            if q.pergunta7 == '2':
                list_4horas[1] += 1
            if q.pergunta7 == '3':
                list_4horas[2] += 1
            if q.pergunta7 == '4':
                list_4horas[3] += 1
            if q.pergunta7 == '5':
                list_4horas[4] += 1

        elif q.pergunta8 == '5':

            if q.pergunta7 == '1':
                list_4horas_mais[0] += 1
            if q.pergunta7 == '2':
                list_4horas_mais[1] += 1
            if q.pergunta7 == '3':
                list_4horas_mais[2] += 1
            if q.pergunta7 == '4':
                list_4horas_mais[3] += 1
            if q.pergunta7 == '5':
                list_4horas_mais[4] += 1

    context['quests'] = quests
    context['list_1hora'] = list_1hora
    context['list_2horas'] = list_2horas
    context['list_3horas'] = list_3horas
    context['list_4horas'] = list_4horas
    context['list_4horas_mais'] = list_4horas_mais


    return render(request,'rel_dif_temp.html', context)


