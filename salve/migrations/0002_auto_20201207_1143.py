# Generated by Django 3.1.4 on 2020-12-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='pergunta1',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='pergunta    1 '),
        ),
        migrations.AlterField(
            model_name='quest',
            name='pergunta2',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='pergunta     2'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='pergunta3',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='pergunta    3'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='pergunta4',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='pergunta     4'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='pergunta5',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='pergunta      5'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='pergunta6',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='pergunta      6'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='pergunta7',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='pergunta   7'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='pergunta8',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='pergunta       8'),
        ),
        migrations.AlterField(
            model_name='quest',
            name='pergunta9',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='pergunta        9'),
        ),
    ]
