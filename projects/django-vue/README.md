## Развертывание
### Backend
1) В корне запускаем `docker-compose up`, если не стоит postgres
2) В `back/app/config` изменяем `example.yml` на `config.yml` со своими данными для postgres
3) В `back/` создаем окружение `python3.9 -m venv venv` и активируем его
4) Ставим dev зависимости `python3.9 -m pip install -r dev_requirements.txt`
5) Переходим в `back/app/` и проводим миграции `python manage.py makemigrations && python manage.py migrate`
6) Запускаем приложение `python manage.py runserver`
* Без сбилженного фронта `http://127.0.0.1:8000/` будет выдавать ошибку

### Frontend
1) Переходим во `front/`, устанавливаем зависимости `npm install`
2) Билдим фронтенд в django `npm run build`
3) Приложение билдится в директории `back/app/static/` и `back/app/templates/`
и становится доступно из django по `http://127.0.0.1:8000/`
