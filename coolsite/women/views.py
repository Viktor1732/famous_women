from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]


class WomenHome(ListView):  # ListView - Отображает ввиде списка
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):  # Делаю чтобы отображались только опубликованные статьи
        return Women.objects.filter(is_published=True)


# def index(request):
#     posts = Women.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ошибка 404. Страница не найдена...</h1>')


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()  # Если форма связана с моделью, то для сохранения достаточно записать так
#             return redirect('home')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

class AddPage(CreateView): # Класс для добавления, например, поста
    form_class = AddPostForm  # AddPostForm - класс формы, который будет подключаться к классу вида
    template_name = 'women/addpage.html'
    # success_url = reverse_lazy('home') - если хотим перенаправить послес добавления статьи в другое место

    def get_context_data(self, *, object_list=None, **kwargs):  # для отображения меню и заголовка
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Famous women'})


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': 'post.title',
#         'cat_selected': post.cat_id,
#     }
#
#     return render(request, 'women/post.html', context=context)

class ShowPost(DetailView):  # DetailView служит, например, для отображения постаъ
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'  # прописывается переменная для слага (для url.py)
    # pk_url_kwarg = 'post.pk' Если использовать ID вместо слаг
    context_object_name = 'post'  # определили переменную (для post.html)

    def get_context_data(self, *, object_list=None, **kwargs):  # для отображения меню и заголовка
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'women/index.html', context=context)

class WomenCategory(ListView):  # ListView - Отображает ввиде списка
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False  # Если установлен False, будет появляться исключение 404

    def get_queryset(self):  # Делаю чтобы отображались только опубликованные статьи
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context
