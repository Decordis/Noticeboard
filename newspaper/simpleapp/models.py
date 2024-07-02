from django.db import models
from django.urls import reverse


class Post(models.Model):
    news = 'NW'
    articles = 'AR'

    CHANGE = [
        (news, 'Новость'),
        (articles, ' Статья')
    ]

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='news')
    post_type = models.CharField(max_length=2, choices=CHANGE, default=articles)


    def __str__(self):
        return f'{self.title.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()

