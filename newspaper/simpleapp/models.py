from django.db import models



# Товар для нашей витрины
class News(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='news')
    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'




class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()

