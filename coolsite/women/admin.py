from django.contrib import admin

from women.models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')  # эти поля будут отображаться в админ-панели
    list_display_links = ('id', 'title')  # поля на которые мы можем кликнуть и перейти для редактирования
    search_fields = ('title', 'content')  # по каким полям можно будет делать поиск
    list_editable = ('is_published',)  # список полей, которые будут редактируемые
    list_filter = ('is_published', 'time_create')  # поля по которым сможе фильтровать список статей


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
