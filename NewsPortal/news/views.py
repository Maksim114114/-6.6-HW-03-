# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
# from django.views.generic import ListView
from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime



class PostsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    # ordering = 'title'
    ordering = '-time_in_post'
    template_name = 'posts.html'
    context_object_name = 'posts'



    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    #метод для изображение времени в шаблоне
    def get_context_data(self, **kwargs):#get_context_data, позволяет нам получить дополнительные данные, которые будут переданы в шаблон.
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['news_count'] = self.get_queryset().count()###добавил показывает количество новостей
        context['time_now'] = datetime.utcnow()


        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        # context['next_sale'] = None
        return context

    # def get_queryset(self):
    #     # показываем только новости в порядке убывания даты публикации
    #     return Post.objects.filter(post_type='1').order_by('-input_time_in_post')
    #     # return Post.objects.all()
    # #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['news_count'] = self.get_queryset().count()
    #     return context






# class PostsDetail(DetailView):#показывает по id ключу  по ссылке news\urls.py  path('<int:pk>', PostsDetail.as_view()),
#     # Модель всё та же, но мы хотим получать информацию по отдельному товару
#     model = Post
#     # Используем другой шаблон — product.html
#     template_name = 'posts.html'
#     # Название объекта, в котором будет выбранный пользователем продукт
#     context_object_name = 'posts'


class PostsDetail(DetailView):#показывает по id ключу  по ссылке news\urls.py  path('<int:pk>', PostsDetail.as_view()),
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'postsid.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'postsid'







class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    # ordering = 'title'
    ordering = '-time_in_post'
    template_name = 'news.html'
    context_object_name = 'news'



    # Метод get_context_data позволяет нам изменить набор данных,
    # который будет передан в шаблон.
    #метод для изображение времени в шаблоне
    def get_context_data(self, **kwargs):#get_context_data, позволяет нам получить дополнительные данные, которые будут переданы в шаблон.
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['news_count'] = self.get_queryset().count()###добавил показывает количество новостей
        context['time_now'] = datetime.utcnow()


        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        # context['next_sale'] = None
        return context


class NewsidDetail(
    DetailView):  # показывает по id ключу  по ссылке news\urls.py  path('<int:pk>', PostsDetail.as_view()),
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'newsid.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'newsid'