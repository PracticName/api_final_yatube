# api_final версия v1
## Описание
Данный API (версия v1) предназначен для работы с проектом Yatube.
API предоставляет возможность зарегестрированным пользователям использовать весь функционал блога Yatube (добавлять и удалять посты, просматривать комментарии поста и т.д.) через ваше приложение.
Незарегистрированные пользователи могут только просматривать ресурсы, но не могут вносить изменения (Подробности в гл. __Примеры__).

### Как подключиться к API:
1. _Выбрать сервис с API._ Найдите сервис, который предоставляет данные, которые вы хотите использовать на своем сайте.
   (Доступные сервисы - см. __Примеры__)
2. _Получить токен_ (```/api/v1/jwt/create/```).
3. _Ознакомиться с главой __Примеры__ документации API._ Изучите доступные методы, форматы запросов и ответов, а также ограничения на использование API.
4. _Использовать библиотеку или написать код для работы с API._ В зависимости от языка программирования и фреймворка, который вы используете,
   вы можете найти готовую библиотеку для работы с API или написать свой код.

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```git clone https://github.com/PracticName/api_final_yatube.git```

```cd api_final_yatube```

Cоздать и активировать виртуальное окружение:

```python -m venv env```

```source env/Scripts/activate```

Установить зависимости из файла requirements.txt:

```python -m pip install --upgrade pip```

```pip install -r requirements.txt```

Выполнить миграции:

```python manage.py migrate```

Запустить проект:

```python manage.py runserver```

## Примеры
- Получение публикаций
  Получить список всех публикаций. При указании параметров limit и offset выдача будет работать с пагинацией. 
  GET ```/api/v1/posts/```
  
  **Ответ**
```
  {
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}  
```
- Создание публикации
  Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
  POST ```/api/v1/posts/```
  
  **Схема запроса**
  text (required) - _string_ (текст публикации)
  image	- _string or null <binary>_
  group	- _integer or null_ (id сообщества)

  **Ответ**
```
  {
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
  }
```
- Получение публикации
  Получение публикации по id.
  GET ```/api/v1/posts/{id}/```
  
  **Параметр пути**
  id (required) - _integer_ id публикации

  **Ответ**
  ```
  {
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
  }
  ```
- Обновление публикации
  Обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
  PUT ```/api/v1/posts/{id}/```
  
  **Параметр пути**
  id (required) - _integer_ id публикации
  
  **Схема запроса**
  text (required) - _string_ (текст публикации)
  image	- _string or null <binary>_
  group	- _integer or null_ (id сообщества)

  **Ответ**
  ```
  {
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
  }
  ```
- Частичное обновление публикации
  Частичное обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.
  PATCH ```/api/v1/posts/{id}/```
  
  **Параметр пути**
  id (required) - _integer_ id публикации
  
  **Схема запроса**
  text (required) - _string_ (текст публикации)
  image	- _string or null <binary>_
  group	- _integer or null_ (id сообщества)

  **Ответ**
  ```
  {
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
  }
  ```
- Удаление публикации
  Удаление публикации по id. Удалить публикацию может только автор публикации. Анонимные запросы запрещены.
  DELETE ```/api/v1/posts/{id}/```
  
  **Параметр пути**
  id (required) - _integer_ id публикации.

- Получение комментариев
  Получение всех комментариев к публикации.
  GET ```/api/v1/posts/{post_id}/comments/```
  
  **Параметр пути**
  post_id (required) - _integer_ id публикации

  **Ответ**
  ```
  [
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
  ]
  ```
- Добавление комментария
  Добавление нового комментария к публикации. Анонимные запросы запрещены.
  POST ```api/v1/posts/{post_id}/comments/```
    
  **Параметр пути**
  post_id (required) - _integer_ id публикации

  **Схема запроса**
  text (required) - _string_ (текст комментария)

  **Ответ**
  ```
  {
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
  }
  ```
- Получение комментария
  Получение комментария к публикации по id.
  GET ```/api/v1/posts/{post_id}/comments/{id}/```
  
  **Параметр пути**
  post_id (required) - _integer_ id публикации
  id (required) - _integer_ id комментария

  **Ответ**
  ```
  {
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
  }
  ```
- Обновление комментария
  Обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
  PUT ```/api/v1/posts/{post_id}/comments/{id}/```
    
  **Параметр пути**
  post_id (required) - _integer_ id публикации
  id (required) - _integer_ id комментария

  **Схема запроса**
  text (required) - _string_ (текст комментария)

  **Ответ**
  ```
  {
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
  }
  ```
- Частичное обновление комментария
  Частичное обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
  PATCH ```/api/v1/posts/{post_id}/comments/{id}/```
  
  **Параметр пути**
  post_id (required) - _integer_ id публикации
  id (required) - _integer_ id комментария

  **Схема запроса**
  text (required) - _string_ (текст комментария)

  **Ответ**
   ```
  {
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
  }
  ```

- Удаление комментария
  Удаление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
  DELETE ```/api/v1/posts/{post_id}/comments/{id}/```
  
  **Параметр пути**
  post_id (required) - _integer_ id публикации
  id (required) - _integer_ id комментария
  
- Список сообществ
  Получение списка доступных сообществ.
  GET ```/api/v1/groups/```
  
  **Ответ**
  ```
  [
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
  ]
  ```
- Информация о сообществе
  Получение информации о сообществе по id.
  GET ```/api/v1/groups/{id}/```
  
  **Параметр пути**
  id (required) - _integer_ id сообщества

  **Ответ**
  ```
  {
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
  }
  ```
- Подписки
  Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.
  Возможен поиск по подпискам по параметру _search_
  GET ```/api/v1/follow/```
  
  **Ответ**
  ```
  [
  {
    "user": "string",
    "following": "string"
  }
  ]
  ```
- Подписка
  Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.
  POST ```/api/v1/follow/```
  
  **Схема запроса**
  following (required) - string (username)

  **Ответ**
  ```
  {
  "user": "string",
  "following": "string"
  }
  ```

- Получить JWT-токен
  POST ```/api/v1/jwt/create/```

  **Схема запроса**
  username (required) - _string_
  password (required) - _string_

  **Ответ** 
  ```
  {
  "refresh": "string",
  "access": "string"
  }
  ```

- Обновить JWT-токен
  POST ```/api/v1/jwt/refresh/```

  **Схема запроса**
  refresh (required) - _string_

  **Ответ** 
  ```
  {
  "access": "string"
  }
  ```
- Проверить JWT-токен
  POST ```/api/v1/jwt/verify/```

  **Схема запроса**
  token (required) - _string_




