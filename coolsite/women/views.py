from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
    return HttpResponse('Главная страница!')

def index(request):
    return HttpResponse("Страница приложения women")

def categories(request):
    return HttpResponse("<h1>Статьи по категорям</h1>")
