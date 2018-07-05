from django import forms
from base.models import Test


class MyTestForm(forms.ModelForm):

    class Meta:
        model = Test  # Модель с какой работает форма
        exclude = [""] # Поля которые необходимо исключить, если не указать, покажет все
