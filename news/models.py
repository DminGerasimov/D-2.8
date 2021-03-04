from django.db import models
from django.contrib.auth.models import user

# Create your models here.
class Author(models.Model):
    # Поле встроенного пользователя User from django.contrib.auth.models
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    # Поле рейтинга автора
    rating = models.FloatField(default = 0)


class Category(models.Model):
    # Категория новостей, статей - уникальная
    news_category = models.CharField(max_length = 24, unique = True)
   


class Post(models.Model):
    # Сведения об авторе публикации: один ко многим с моделью Author
    author = models.ForeignKey('Author', on_delete = models.CASCADE)

    # Выбор вида публикации: статья, новость фиксированная двумя значениями
    news, article = 'NE', 'AR'
    POSITIONS = [(news, 'Новость'), (article,'Статья')]
    type_news_article = models.CharField(max_length = 2, choices = POSITIONS, default = news)

    # Дата создания публикации
    time_in = models.DateTimeField(auto_now_add = True)

    # Заголовок статьи/новости
    chapter = models.CharField(max_length = 200, unique = False)
    # Текст статьи/новости
    # chapter = models.TextField(max_length = 200, unique = False)
    # Рейтинг статьи/новости

    # Связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory)


class PostCategory(models.Model):
    # Связь «один ко многим» с моделью Post

    # Связь «один ко многим» с моделью Category


class Comment(models.Model):
    # Связь «один ко многим» с моделью Post

    # Связь «один ко многим» с встроенной моделью User /
    # (комментарии может оставить любой пользователь, не обязательно автор)

    # Текст комментария

    # Дата и время создания комментария

    # Рейтинг комментария