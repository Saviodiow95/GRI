from django.contrib import admin

# Register your models here.
from questionario.models import Quest


class QuestAdmin(admin.ModelAdmin):
    list_display = ('email', 'nome', 'grau', 'curso', 'turma',)
    list_filter = ('grau', 'curso', 'turma',)

admin.site.register(Quest,QuestAdmin)