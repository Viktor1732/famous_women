from django import template

from women.models import *

register = template.Library()  # Создаем экземпляр, через который происходит регистрация собственных шаблонов


@register.simple_tag(name='getcats')  # превращем функцию в тег
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')  # включающий тег, в скобках прописываем адрес шаблона
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}

