from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    # Поле встроенного пользователя User from django.contrib.auth.models
    user_author = models.OneToOneField(User, on_delete = models.CASCADE)

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
    chapter = models.TextField()
    # Рейтинг статьи/новости
    article_news_rate = models.FloatField(default=0.0)
    # Связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory)
    category = models.ManyToManyField(Category, through= 'PostCategory')

class PostCategory(models.Model):
    # Связь «один ко многим» с моделью Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # Связь «один ко многим» с моделью Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    # Связь «один ко многим» с моделью Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # Связь «один ко многим» с встроенной моделью User /
    # (комментарии может оставить любой пользователь, не обязательно автор)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Текст комментария
    comment_text = models.TextField(help_text='Текст комментария', default='')
    # Дата и время создания комментария
    time_creation = models.DateTimeField(auto_now_add=True)
    # Рейтинг комментария
    comment_rate = models.FloatField(default=0.0)