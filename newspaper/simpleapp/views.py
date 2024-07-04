from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import NewsFilter
from .models import Post
from .forms import PostForm


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов, чтобы свежая дата была нужно написать '-date'
    ordering = '-date'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'flatpages/news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'post'
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

class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной статье/новости
    model = Post
    # Используем другой шаблон — 'flatpages/article.html'
    template_name = 'flatpages/article.html'
    # Название объекта, в котором будет выбранный пользователем cтатья
    context_object_name = 'post'

class PostSearch(ListView):
    model = Post
    template_name = 'flatpages/news_search.html'
    context_object_name = 'post'
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

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path =='/news/article/create/':
            post.post_type = 'AR'
        post.save()
        return super().form_valid(form)

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'flatpages/news_delete.html'
    successPost = reverse_lazy('post_list')







