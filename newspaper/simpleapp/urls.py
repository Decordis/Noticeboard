from django.urls import path

from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete

urlpatterns = [
# path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
    path('', PostList.as_view(), name='news_list'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', PostDetail.as_view(), name='news_detail'),
    path('search/', PostSearch.as_view(), name='news_search'),
    path('create/', PostCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='news_edit'),
    path('<int:pk>/delete', PostDelete.as_view(), name='news_delete'),
    path('article/create/', PostCreate.as_view(), name='news_create'),
    path('article/<int:pk>/update/', PostUpdate.as_view(), name='news_edit'),
    path('article/<int:pk>/delete', PostDelete.as_view(), name='news_delete'),


]