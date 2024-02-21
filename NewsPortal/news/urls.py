from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList
from .views import PostsList, PostsDetail,NewsidDetail


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostsList.as_view()),
# pk — это первичный ключ товара, который будет выводиться у нас в шаблон
# int — указывает на то, что принимаются только целочисленные значения
   #path('<int:pk>',PostsDetail.as_view()),
   #path('<int:id>', PostsDetail.as_view()),
  # path('<int:pk>', PostsDetail1.as_view()),
   path('<int:pk>/', PostsDetail.as_view()),
   path('news/<int:pk>/', PostsDetail.as_view(), name='posts_detail'),
   path('<int:pk>/', NewsidDetail.as_view()),
]