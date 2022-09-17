# Прописываем все модели для взаимодействия с БД
from django.db import models
from django.urls import reverse


class Women(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='ЗАГОЛОВОК')  # verbose-name - название для заголовка в админ-панели.
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='НАЗВАНИЕ СТАТЬИ') # blank=True - необязательно для заполнения
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')  # id к cat - django добавит автоматически

    def __str__(self):  # Для взаимодействия модели с базой данных через python manage.py shell
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'  # изменяет название класса в админ-панели
        verbose_name_plural = 'Известные женщины'  # чтобы уюрать 's' в названии класса
        ordering = ['-time_create', 'title']  # порядок сортировки в админ-панели


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='КАТЕГОРИЯ')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'КАТЕГОРИЯ'  # изменяет название класса в админ-панели
        verbose_name_plural = 'КАТЕГОРИИ'  # чтобы уюрать 's' в названии класса
        ordering = ['id']  # порядок сортировки в админ-панели
