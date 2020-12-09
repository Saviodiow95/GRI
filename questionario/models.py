from django.db import models



# Create your models here.
class Quest(models.Model):

    perg = {}
    TEXT_HELP=" (Responda 1 para Péssimo e 5 para Ótimo)"

    RESP_CHOICE =(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )

    TEMP_CHOICE =(
        ('1', '1 hora'),
        ('2', '2 horas'),
        ('3', '3 horas'),
        ('4', '4 horas'),
        ('5', 'Mais de 4 horas')
    )

    TURMA_CHOICE =(
        ('1','0120'),
        ('2','0119'),
        ('3','0118'),
        ('4','0117'),
        ('5','0116'),
        ('6','0115'),
        ('7','0114')
    )

    CURSO_CHOICE =(
        ('1','Análise e Desenvolvimento de Sistemas - ADS'),
        ('2','Engenharia Agronômica'),
        ('3','Tecnologia em Processos Gerenciais'),
        ('4','Técnico em Administração Integrado ao Ensino Médio'),
        ('5','Técnico em Agropecuária Integrado ao Ensino Médio'),
        ('6','Técnico Agropecuária Integrado ao Ensino Médio em Regime de Alternância'),
        ('7','Técnico em Informática Integrado ao Ensino Médio'),
        ('8','Técnico em Zootecnia Integrado ao Ensino Médio'),
        ('9','Técnico em Enfermagem Subsequente')
    )

    GRAU_CHOICE =(
        ('1', 'Superior'),
        ('2', 'Técnico')
    )

    perg['1'] ="Como as ANP's contribuíram para o seu aprendizado?"+TEXT_HELP

    perg['2'] ="Em seu ponto de vista,o formato de aula remota que o IFNMG propôs gera conexão entre aluno e o instituto?"+TEXT_HELP

    perg['3'] ="Em seu ponto de vista,as aulas remotas foram importantes e efetivas?"+TEXT_HELP

    perg['4'] ="Avalie sua satisfação em relação às atividades remotas?"+TEXT_HELP

    perg['5'] ="Você acredita que os meios de comunicação usados pelo IFNMG neste momento de distanciamento social para compartilhar informações gerais foram eficientes?"+TEXT_HELP

    perg['6'] ="Como você classifica o conteúdo e o tipo de material que está estudando?"+TEXT_HELP

    perg['7'] ="Qual é o nível de dificuldade que você tem em estudar a distância?"+TEXT_HELP

    perg['8'] ="Quantas horas no mínimo você estuda o material disponibilizado para o seu curso?"

    perg['9'] ="Como você avalia o processo de orientação e acompanhamento dos professores, ao longo dos modulos? "+TEXT_HELP

    email = models.CharField(max_length=200, verbose_name="Email", unique=True)
    nome = models.CharField(max_length=200, verbose_name="Nome Completo")
    grau = models.CharField(max_length=1, choices=GRAU_CHOICE, verbose_name="Tipo de Ensino ?")
    curso = models.CharField(max_length=1, choices=CURSO_CHOICE, verbose_name="Qual é o seu curso?")
    turma = models.CharField(max_length=1, choices=TURMA_CHOICE, verbose_name="Qual a sua Turma?")

    pergunta1 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['1'])
    pergunta2 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['2'])
    pergunta3 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['3'])
    pergunta4 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['4'])
    pergunta5 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['5'])
    pergunta6 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['6'])
    pergunta7 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['7'])
    pergunta8 = models.CharField(max_length=1, choices=TEMP_CHOICE, verbose_name=perg['8'])
    pergunta9 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['9'])
