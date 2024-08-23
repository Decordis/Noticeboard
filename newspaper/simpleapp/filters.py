import django_filters
from django import forms
from django_filters import FilterSet
from .models import Post


class NewsFilter(FilterSet):
    date = django_filters.DateFilter(
        field_name='date',
        widget=forms.DateTimeInput(attrs={'type': 'date'}),
        label='Дата', lookup_expr='date__gte'
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
        }
