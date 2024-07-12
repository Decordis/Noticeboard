from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        post_rating = Post.objects.filter(auth=self).aggregate(pr=Coalesce(Sum('rating'), 0))['pr']
        comments_rating = Comment.objects.filter(user=self.user).aggregate(cr=Coalesce(Sum('rating'), 0))['cr']
        posts_comments_rating = Comment.objects.filter(post__auth=self).aggregate(pcr=Coalesce(Sum('rating'), 0))['pcr']

        self.rating = post_rating * 3 + comments_rating + posts_comments_rating
        self.save()

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
    category = models.ManyToManyField(to='Category', through='PostCategory')
    post_type = models.CharField(max_length=2, choices=CHANGE, default=news)
    rating = models.IntegerField(default=0)

    def preview(self):
        return self.description[0:126] + '...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


    def __str__(self):
        return f'{self.title.title()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_text = models.CharField(max_length=2000)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
