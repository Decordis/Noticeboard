from django.db import models



# Товар для нашей витрины
class News(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')

    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='news') # все продукты в категории будут доступны через поле products


    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'



# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()
#Не забываем зарегистрировать модели, иначе мы не увидим их в админке. Заходим в эту же папку simpleapp/admin.py
# Create your models here.


