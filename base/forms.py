from django import forms
from base.models import Test


class MyTestForm(forms.ModelForm):

    class Meta:
        model = Test
        exclude = [""]
