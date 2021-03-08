from django.contrib.auth.models import User
from news.models import Author, Category

# 1. Создать двух пользователей (с помощью метода User.objects.create_user).
u1_name, u2_name = 'User1', 'User2'
User.objects.create_user(username=u1_name, password='easy password')
User.objects.create_user(username=u2_name, password='easy password')

# 2. Создать два объекта модели Author, связанные с пользователями.
Author(user_id=User.objects.all().values().filter(username=u1_name)[0]['id']).save()
Author(user_id=User.objects.all().values().filter(username=u2_name)[0]['id']).save()

# 3. Добавить 4 категории в модель Category.
Category.objects.create(news_category='Спорт')
Category.objects.create(news_category='Досуг')
Category.objects.create(news_category='Погода')
Category.objects.create(news_category='Курс валют')

# 4. Добавить 2 статьи и 1 новость.


# 5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
# 6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
# 7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
# 8. Обновить рейтинги пользователей.
# 9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
# 10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
# 11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.