from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Famous women'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ошибка 404. Страница не найдена...</h1>')


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Famous women'})
