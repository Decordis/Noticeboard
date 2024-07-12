from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'author',
            'category'
        ]

        def clean(self):
            cleaned_data = super().clean()
            description = cleaned_data.get('description')
            if description is not None and len(description)<20:
                raise ValidationError({
                    'description' : 'Описание не может быть меньще 20 символов'
                })

            title = cleaned_data.get('title')
            if title == description:
                raise ValidationError('Описание не должно быть идентичным названию')

            author = cleaned_data.get('author')
            if author is None:
                raise ValidationError('Поле автора не должно быть пустым')

            return cleaned_data