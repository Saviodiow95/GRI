from django import forms

from questionario.models import Quest


class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = '__all__'