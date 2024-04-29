# sport_channel

sport_channel - веб приложение с каталогом новостей и магазином спорттоваров. Реализована система регистрации и авторизации пользователей, система комментариев, публикация товаров.

# Руководство по запуску

+ Клонируйте репозиторий
+ Создайте виртуальное окружение и активируйте его:

#### Windows
```
> python -m venv .venv
> .venv\Scripts\activate
```

#### Linux
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

+ На вашей операционой системе должен быть установлен PostgreSQL
+ Создайте базу данных sport_db в PotgreSQL
+ Проведите миграции командой:

#### Windows
```
> python manage.py migrate
```

#### Linux
```
$ python3 manage.py migrate
```

+ Создайте суперпользователя для  входа в админ панель:

#### Windows
```
> python manage.py createsuperuser
```

#### Linux
```
$ python3 manage.py createsuperuser
```

+ Запустите приложение:

#### Windows
```
> python manage.py runserver
```

#### Linux
```
$ python3 manage.py runserver
```

+ Откройте браузер и перейдите по адресу http://127.0.0.1:8000/main/. Поздравляю, теперь вы можете пользоваться моим приложением :wink:


## Главная страница
![](https://github.com/GGGamzat/sport_channel/blob/main/images/1.png)

# Автор

Абдуллаев Гамзат