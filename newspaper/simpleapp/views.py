from django.views.generic import ListView, DetailView
from datetime import datetime

from .models import News


class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = News
    # Поле, которое будет использоваться для сортировки объектов, чтобы свежая дата была нужно написать '-date'
    ordering = '-date'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'flatpages/news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'


# Далее указываем путь к нашему классу, для начала создаем в simpleapp urls.py

class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной статье/новости
    model = News
    # Используем другой шаблон — 'flatpages/article.html'
    template_name = 'flatpages/article.html'
    # Название объекта, в котором будет выбранный пользователем cтатья
    context_object_name = 'new'

    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.



