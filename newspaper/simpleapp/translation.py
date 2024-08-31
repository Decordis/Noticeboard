from .models import Post, Category
from modeltranslation.translator import register, TranslationOptions


# импортируем декоратор для перевода и класс настроек, от которого будем наследоваться

# регистрируем модели для перевода
@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)  # Перечисляем поля для перевода


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

# заходим в админку и регистрируемся
