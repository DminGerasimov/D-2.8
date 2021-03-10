from django.contrib.auth.models import User
from news.models import *

# 1. Создать двух пользователей (с помощью метода User.objects.create_user).
u1_name, u2_name = 'User1', 'User2'
User.objects.create_user(username=u1_name, password='easy password')
User.objects.create_user(username=u2_name, password='easy password')

# 2. Создать два объекта модели Author, связанные с пользователями.
a1 = Author.objects.create(user_id=User.objects.all().values().filter(username=u1_name)[0]['id'])
a2 = Author.objects.create(user_id=User.objects.all().values().filter(username=u2_name)[0]['id'])

# 3. Добавить 4 категории в модель Category.
cat1 = Category.objects.create(news_category='Спорт')
cat2 = Category.objects.create(news_category='Досуг')
cat3 = Category.objects.create(news_category='Погода')
cat4 = Category.objects.create(news_category='Курс валют')

# 4. Добавить 2 статьи и 1 новость.
p1 = Post.objects.create(author=a1, type_news_article = 'AR', chapter ='Заголовок первой статьи', text ='Текст первой статьи')
p2 = Post.objects.create(author=a2, type_news_article = 'AR', chapter ='Заголовок второй статьи', text ='Текст второй статьи')
p3 = Post.objects.create(author=a1, type_news_article = 'NE', chapter ='Заголовок новости', text ='Текст новости')

# 5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
p1.category.add(cat1, cat3, cat4)
p2.category.add(cat3, cat4)
p3.category.add(cat2, cat4)

# Проверка присвоения категорий
p1.category.all().values()
p2.category.all().values()
p3.category.all().values()

# 6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
c1 = Comment.objects.create(post = p1, user = a1, comment_text ='1 Комментарий к посту 1 пользователя 1')
c2 = Comment.objects.create(post = p1, user = a1, comment_text ='2 Комментарий к посту 1 пользователя 1')
c3 = Comment.objects.create(post = p2, user = a2, comment_text ='Комментарий к посту 2 пользователя 2')
c4 = Comment.objects.create(post = p3, user = a2, comment_text ='Комментарий к посту 3 пользователя 2')
c5 = Comment.objects.create(post = p3, user = a1, comment_text ='Комментарий к посту 3 пользователя 1')

# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
Comment.objects.all().values('id') #определяем id комментариев
_ = Comment.objects.get(id=1)
_.like()
_.like()
_.like()
_.save()
_ = Comment.objects.get(id=2)
_.like()
_.dislike()
_.dislike()
_.save()
_ = Comment.objects.get(id=3)
_.dislike()
_.dislike()
_.dislike()
_.save()
_ = Comment.objects.get(id=4)
_.like()
_.like()
_.dislike()
_.save()

Post.objects.all().values('id') #определяем id статей\новостей
_ = Post.objects.get(id=13)
_.like()
_.like()
_.like()
_.save()

_ = Post.objects.get(id=14)
_.like()
_.dislike()
_.like()
_.save()

_ = Post.objects.get(id=15)
_.dislike()
_.dislike()
_.dislike()
_.save()

# 8. Обновить рейтинги пользователей.
Author.objects.all().values('id') # определяем id авторов
Author.objects.get(id=7).update_rating()
Author.objects.get(id=8).update_rating()

# 9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
best = Author.objects.all().order_by('-rating').values('user_id','rating')[0]
f"""username: {User.objects.filter(id=int(best['user_id'])).values('username')[0]['username']}"""
f"""rating: {best['rating']}"""

# 10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.


# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.

