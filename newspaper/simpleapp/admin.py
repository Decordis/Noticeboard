from django.contrib import admin
from .models import Post, Category, PostCategory
from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(TranslationAdmin):
    model = Category

class PostAdmin(TranslationAdmin):
    model = Post


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
# Register your models here.
""""
не забудь прописать команду makemigrations, затем migrate, а потом python manage.py update_translation_fields
"""