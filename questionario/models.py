from django.db import models



# Create your models here.
class Quest(models.Model):

    perg = {}
    TEXT_HELP="Responda 1 para Péssimo e 5 para Ótimo"

    RESP_CHOICE =(
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    perg['1'] ="pergunta    1 "
    perg['2'] ="pergunta     2"
    perg['3'] ="pergunta    3"
    perg['4'] ="pergunta     4"
    perg['5'] ="pergunta      5"
    perg['6'] ="pergunta      6"
    perg['7'] ="pergunta   7"
    perg['8'] ="pergunta       8"
    perg['9'] ="pergunta        9"

    email =  models.CharField(max_length=200, verbose_name="Email", unique=True)
    pergunta1 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['1'], help_text=TEXT_HELP)
    pergunta2 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['2'], help_text=TEXT_HELP)
    pergunta3 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['3'], help_text=TEXT_HELP)
    pergunta4 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['4'], help_text=TEXT_HELP)
    pergunta5 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['5'], help_text=TEXT_HELP)
    pergunta6 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['6'], help_text=TEXT_HELP)
    pergunta7 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['7'], help_text=TEXT_HELP)
    pergunta8 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['8'], help_text=TEXT_HELP)
    pergunta9 = models.CharField(max_length=1, choices=RESP_CHOICE, verbose_name=perg['9'], help_text=TEXT_HELP)
