# LeadHit_case
web app with MongoDB

## Depends:
- python 3.10.12,
- docker version 24.0.6, build ed223bc,
- pip 23.3.1
- make 4.3 

## Descriptions:
Web-приложение для определения заполненных форм.

Определяет четыре типа данных полей: 
- email
- телефон
- дата
- текст

На вход по урлу **POST** _http://0.0.0.0:8000/api/hb/get_form?_ запросом передаются данные такого вида:
_f_name1=value1&f_name2=value2_ 
В ответ возвращается имя подходящего шаблона, если такой имеется,
в обратном случае автоматически валидируются входящие значения и отдаются в виде _dict_,
после чего данная форма занится в БД ко всем шаблонам. Совпадающими считаются поля,
у которых совпали имя и тип значения.

Телефон передается в стандартном формате _+7 xxx xxx xx xx_,
дата передается в формате _DD:MM:YYYY._ или _YYYY:MM:DD_.

В качестве БД была использована _MongoDB_, все запросы осущаствляются к ней напрямую.

В качестве фреймоврка для веб-приложения был использован _FastAPI_

Проект содержит в себе инструменты CI (проверка линтеров, прогонка небольших тестов),
при запуске приложения будет создана папка _docker_volumes_ в которой будут храниться данные из БД,
так же будет вестись журнал логирования записывающий ошибки. 

По ссылке _http://0.0.0.0:8000/docs_ можно посмотреть все доступные эндроинты и ознакомиться с ними
благодаря автоматической генерации документации _Swagger_

В проекте реализован небольшой скрипт uor.py для пробрасывания POST запросов к приложению.

## Local start:
1. Активировать виртуальное окружение.
2. `pip install -r requirements.txt` - установить зависимости
3. `make up_local` - поднимет бд и запустит веб приложение
4. `python3 uor.py` - запустит тестовый скрипт, который будет ждать входные данные
5. `make down_local` - для выключения БД

## Docker webapp start:
1. Активировать uorвиртуальное окружение.
2. `pip install -r requirements.txt` - установить виртуальное окружение (Этот пункт можно пропустить, если не будет запускаться uor.py)
3. `make up_uor` - запустит БД и webapp, после чего запустит тестовый скрипт (Этот пункт можно пропустить, если не будет запускаться uor.py)
4. `docker compose -f docker-compose-cd.yaml up -d` - для запуска контейнеров без uor.py
5. `make down_cd` - выключит все контейнеры и удалит образ приложения






