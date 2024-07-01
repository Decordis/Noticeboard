from django.views.generic import ListView, DetailView
from .filters import NewsFilter
from .forms import NewsForm
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
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


# Далее указываем путь к нашему классу, для начала создаем в simpleapp urls.py

class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной статье/новости
    model = News
    # Используем другой шаблон — 'flatpages/article.html'
    template_name = 'flatpages/article.html'
    # Название объекта, в котором будет выбранный пользователем cтатья
    context_object_name = 'new'

class NewsSearch(ListView):
    model = News
    template_name = 'flatpages/news_search.html'
    context_object_name = 'news'
    ordering = '-date'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context





