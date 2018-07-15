from django.shortcuts import render
from .forms import MyTestForm
from django.views.generic import DetailView
from .models import *

def base(request):  

    name = "Zohan"  # Можно отобразить через шаблонизатор  на странице html {{ }}

    # Етой строчки достаточно что бы форма отрисовалась на страницеа
    # Форма сделана на основании модели, и принимает или реквест пост запрос или ничего
    form = MyTestForm(request.POST or None)  # Можно отобразить через шаблонизатор  на странице html {{ }}

    if request.method == "POST" and form.is_valid():
        #data = form.cleaned_data # cleaned_data - метод который дает возможность считать все поля, тут имя и маил
        #print(form.cleaned_data["name"])   # так можем вывести конкретно имя
        new_form = form.save() # пересохраняем форму под новым именем, что бы она не пересохранялась под старым

    return render(request, 'base/home.html', locals()) # С помошью функции рендер возвращаем html шаблон (отрисовуем)


class Show(DetailView):  # класс Detail.View звточен для следующей задачи:
                         # забрать id с url, забрать обьект по id с базы данных, и
                         # отрендерить страницу отдав туда етот обьект

    model = InfoUser
    template_name = "base/base2.html"