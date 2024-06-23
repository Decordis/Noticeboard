from django import template

register = template.Library()

CENSOR = ['Вышло', 'новое', 'задачи', 'глупые', 'математики', 'Elden']

@register.filter()
def censor(value):
    for word in CENSOR:
        value = value.replace(word[1:], '*' * len(word[1:]))
    return value