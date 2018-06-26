from django.shortcuts import render


def base(request):

    name = "Zohan"  # Можно отобразить через шаблонизатор  на странице {{ }}

    return render(request, 'base/home.html', locals()) # С помошью функции рендер возвращаем html шаблон (отрисовуем)