from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def main_page(request):
    return HttpResponse('Главная страница!')

def index(request):
    return HttpResponse("Страница приложения women")

def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категорям</h1><br><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Всё про {year} год</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')