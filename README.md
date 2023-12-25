# api_final версия v1
## Описание
Данный API (версия v1) предназначен для работы с проектом Yatube.

### Доступные ресурсы:
- Получение публикаций 
  GET ```/api/v1/posts/```
  Получить список всех публикаций. При указании параметров limit и offset выдача будет работать с пагинацией.
 
- Создание публикации
  POST ```/api/v1/posts/```
  Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.

- Получение публикации
  GET ```/api/v1/posts/{id}/```
  Получение публикации по id.

- Обновление публикации
  PUT ```/api/v1/posts/{id}/```
  Обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.

 
- Частичное обновление публикации
  PATCH ```/api/v1/posts/{id}/```
  Частичное обновление публикации по id. Обновить публикацию может только автор публикации. Анонимные запросы запрещены.

 
- Удаление публикации
  DELETE ```/api/v1/posts/{id}/```
  Удаление публикации по id. Удалить публикацию может только автор публикации. Анонимные запросы запрещены.

- Получение комментариев
  GET ```/api/v1/posts/{post_id}/comments/```
  Получение всех комментариев к публикации.

- Добавление комментария
  POST ```api/v1/posts/{post_id}/comments/```
  Добавление нового комментария к публикации. Анонимные запросы запрещены.
  
- Получение комментария
  GET ```/api/v1/posts/{post_id}/comments/{id}/```
  Получение комментария к публикации по id.

- Обновление комментария
  PUT ```/api/v1/posts/{post_id}/comments/{id}/```
  Обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
  
- Частичное обновление комментария
  PATCH ```/api/v1/posts/{post_id}/comments/{id}/```
  Частичное обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.

- Удаление комментария
  DELETE ```/api/v1/posts/{post_id}/comments/{id}/```
  Удаление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены.
  
- Список сообществ
  GET ```/api/v1/groups/```
  Получение списка доступных сообществ.

- Информация о сообществе
  GET ```/api/v1/groups/{id}/```
  Получение информации о сообществе по id.

- Подписки
  GET ```/api/v1/follow/```
  Возвращает все подписки пользователя, сделавшего запрос. Анонимные запросы запрещены.
  Возможен поиск по подпискам по параметру _search_

- Подписка
  POST ```/api/v1/follow/```
  Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.

- Получить JWT-токен
  POST ```/api/v1/jwt/create/```

- Обновить JWT-токен
  POST ```/api/v1/jwt/refresh/```

- Проверить JWT-токен
  POST ```/api/v1/jwt/verify/```

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
  DELETE ```/api/v1/posts/{id}/```
  
  **Параметр пути**
  id (required) - _integer_ id публикации.

- Получение комментариев
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
  DELETE ```/api/v1/posts/{post_id}/comments/{id}/```
  
  **Параметр пути**
  post_id (required) - _integer_ id публикации
  id (required) - _integer_ id комментария
  
- Список сообществ
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




