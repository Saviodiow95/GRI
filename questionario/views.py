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

    perg4_sup  = [0, 0, 0, 0, 0]
    perg4_tec  = [0, 0, 0, 0, 0]

    sup_ads = list(Quest.objects.filter(curso='1'))
    sup_eng = list(Quest.objects.filter(curso='2'))
    sup_pg = list(Quest.objects.filter(curso='3'))

    tec_adm = list(Quest.objects.filter(curso='4'))
    tec_agr = list(Quest.objects.filter(curso='5'))
    tec_alt = list(Quest.objects.filter(curso='6'))
    tec_inf = list(Quest.objects.filter(curso='7'))
    tec_zoo = list(Quest.objects.filter(curso='8'))
    tec_enf = list(Quest.objects.filter(curso='9'))


    for q in superior:
        if q.pergunta4 == '1':
            perg4_sup[0] +=1

        elif q.pergunta4 == '2':
            perg4_sup[1] += 1

        elif q.pergunta4 == '3':
            perg4_sup[2] += 1

        elif q.pergunta4 == '4':
            perg4_sup[3] += 1

        elif q.pergunta4 == '5':
            perg4_sup[4] += 1

    for q in tecnico:
        if q.pergunta4 == '1':
            perg4_tec[0] += 1

        elif q.pergunta4 == '2':
            perg4_tec[1] += 1

        elif q.pergunta4 == '3':
            perg4_tec[2] += 1

        elif q.pergunta4 == '4':
            perg4_tec[3] += 1

        elif q.pergunta4 == '5':
            perg4_tec[4] += 1





    context['quests'] = quests
    context['superior'] = superior
    context['tecnico'] = tecnico

    context['qtd_ads'] = len(sup_ads)
    context['qtd_eng'] = len(sup_eng)
    context['qtd_pg'] = len(sup_pg)

    context['qtd_adm'] = len(tec_adm)
    context['qtd_agr'] = len(tec_agr)
    context['qtd_alt'] = len(tec_alt)
    context['qtd_inf'] = len(tec_inf)
    context['qtd_zoo'] = len(tec_zoo)
    context['qtd_enf'] = len(tec_enf)


    context['perg4_sup'] = perg4_sup
    context['perg4_tec'] = perg4_tec






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


