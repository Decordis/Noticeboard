from django import forms
from django.core.exceptions import ValidationError
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'name',
            'description',
            'author',
            'date',
            'category'
        ]

        def clean(self):
            cleaned_data = super().clean()
            description = cleaned_data.get('description')
            if description is not None and len(description)<20:
                raise ValidationError({
                    'description' : 'Описание не может быть меньще 20 символов'
                })

            name = cleaned_data.get('name')
            if name == description:
                raise ValidationError('Описание не должно быть идентичным названию')

            author = cleaned_data.get('author')
            if author is None:
                raise ValidationError('Поле автора не должно быть пустым')

            return cleaned_data