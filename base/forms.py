from django import forms
from base.models import InfoUser


class MyTestForm(forms.ModelForm):

    class Meta:
        model = InfoUser  # Модель с какой работает форма
        exclude = [""] # Поля которые необходимо исключить, если не указать, покажет все
