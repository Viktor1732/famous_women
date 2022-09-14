from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связье', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ошибка 404. Страница не найдена...</h1>')


def addpage(request):
    return HttpResponse('Добавить статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Famous women'})


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id: {post_id}')