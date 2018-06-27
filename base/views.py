from django.shortcuts import render
from .forms import MyTestForm

def base(request):

    name = "Zohan"  # Можно отобразить через шаблонизатор  на странице {{ }}

    form = MyTestForm(request.POST or None)

    if request.method =="POST" and form.is_valid():
        data = form.cleaned_data
        new_form = form.save()

    return render(request, 'base/home.html', locals()) # С помошью функции рендер возвращаем html шаблон (отрисовуем)