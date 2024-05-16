![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-D82C20?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Alembic](https://img.shields.io/badge/Alembic-336791?style=for-the-badge)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-003545?style=for-the-badge&logo=sqlalchemy)
![Pydantic](https://img.shields.io/badge/Pydantic-2D3748?style=for-the-badge&logo=pydantic)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens)
![Celery](https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery)
![Flower](https://img.shields.io/badge/Flower-306998?style=for-the-badge&logo=flower)
![Prometheus](https://img.shields.io/badge/Prometheus-000000?style=for-the-badge&logo=prometheus)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Sentry](https://img.shields.io/badge/Sentry-362D59?style=for-the-badge&logo=sentry&logoColor=white)
<p align="center">
  <img src="https://github.com/Progger715/Booking-Api/assets/83240866/74dece53-d080-4e7e-800e-34eff7d9df90" alt="альтернативный текст">
</p>

# Оглавление

- [Описание проекта](#описание-проекта)
- [Технологии](#технологии)
- [Установка и запуск](#Установка-и-запуск)
- [Конфигурация](#конфигурация)
- [API Endpoints](#API-Endpoints)
- [Документация API](#Документация-API)
- [Тестирование](#Тестирование)


# Описание проекта

Проект представляет api для бронирования отелей, разработанное с использованием FastAPI. Основной функционал конечного
пользователя:

* Регистрация в приложении;
* Аутентификация в приложении;
* Выход из аккаунта в приложении;
* Просмотр информации о своем аккаунте;
* Поиск отелей по различным критериям (локация, даты заезда и выезда);
* Просмотр комнат интересующего отеля;
* Просмотр информации об отелях, включая фотографии, описания, удобства.
* Бронирование номеров в отелях;
* Получение уведомлений о бронировании на почту;
* Просмотр собственных броней;
* Отмена брони.

# Технологии

- **FastAPI** - используется для создания REST API. FastAPI поддерживает асинхронную обработку запросов и
  автоматическую генерацию документации.

- **SQLAlchemy** - ORM, позволяющая взаимодействовать с базой данных с использованием объектно-ориентированного
  подхода. Упрощает выполнение операций с базой данных.

- **PostgreSQL** - объектно-реляционная система управления базами данных, используемая для хранения данных о
  пользователях, отелях и бронированиях.

- **Pydantic** - используется для валидации и управления данными с использованием аннотаций типов Python.
  Обеспечивает строгую типизацию и валидацию входящих данных для API.

- **JWT (JSON Web Tokens)** - используется для аутентификации и авторизации пользователей, позволяя безопасно
  передавать информацию между клиентом и сервером.

- **Celery** - асинхронная очередь задач, используемая для выполнения фоновых задач, таких как, например,
  отправка электронных писем.

- **Flower** - веб-интерфейс для мониторинга и управления задачами Celery. Используется для отслеживания состояния
  задач и работы воркеров.

- **Redis** - система управления базами данных в памяти, используемая в качестве брокера сообщений для Celery и для
  кэширования данных, чтобы ускорить загрузку часто запрашиваемой информации.

- **Docker** - используется для запуска приложений в контейнерах. Упрощает развертывание и управление приложением,
  обеспечивая его изоляцию от окружения.

- **Docker Compose** - используется для определения и запуска многоконтейнерного приложения Docker. Упрощает
  конфигурацию и управление контейнерами.

- **Alembic** - инструмент для миграции баз данных, позволяющий версионировать и применять изменения в схеме базы
  данных.

- **Pytest** - фреймворк для написания и выполнения тестов. Используется для unit и integration тестирования.

- **Jinja2** - шаблонизатор для Python, позволяющий создавать динамические веб-страницы. Используется для генерации
  HTML-шаблонов.

- **Admin Panel** - интерфейс администратора, обеспечивающий удобное управление данными и настройками приложения.

- **Prometheus** - система мониторинга и оповещения, используется для наблюдения за работой приложения в
  реальном времени.

- **Grafana** - инструмент для визуализации и анализа данных, используется для мониторинга
  производительности приложений и систем, по средствам создания информативного дашборда.

- **Sentry** - система отслеживания ошибок, используется для отслеживания и оповещении о проблемах в реальном времени.

# Установка и запуск

1. Клонируйте репозиторий:

```plaintext
   git clone https://github.com/Progger715/Booking-Api.git
```

2. Перейдите в директорию проекта:

```plaintext
   cd Booking-Api
```

3. Создайте файл для переменных окружения

  ```bash
echo > app\config\.env
  ```

После чего заполните данный файл любым удобным для вас способом в соответствии с
разделом [конфигурация](#конфигурация-приложения-fastAPI)

## Варианты запуска:

### 1. веб-сервер uvicorn

Для запуска FastAPI можно использовать веб-сервер uvicorn. Команда для запуска:

```bash
uvicorn app.main:app --reload
```  

Необходимо запускать команду, находясь в корневой директории проекта.

После чего нужно вручную запустить все сопутствующие инструменты:

* Celery

Для запуска Celery используется команда:

```bash
celery --app=app.tasks.celery:celery worker -l INFO -P solo
```

Обратите внимание, что `-P solo` используется только на Windows, так как у Celery есть проблемы с работой на Windows.

* Flower

Для запуска Flower используется команда

```bash
celery --app=app.tasks.celery:celery flower
``` 

После выполнения всех трех команд, приложение будет доступно по адресу **http://localhost:8000**
Flower будет доступно по адресу **http://localhost:5555**

### 2. Dockerfile

Для запуска веб-сервера (FastAPI) внутри контейнера необходимо иметь уже запущенный экземпляр PostgreSQL на компьютере.
Код для запуска Dockerfile:

```bash
docker build .
```  

Команда также запускается из корневой директории, в которой лежит файл Dockerfile.

### 3. Docker compose

Для запуска всех сервисов (БД, Redis, веб-сервер (FastAPI), Celery, Flower, Grafana, Prometheus) необходимо:

* создать файл .env-non-dev для переменных окружения docker compose. И заполнить его любым удобным
  для вас способом в соответствии с разделом [конфигурация](#конфигурация-приложения-docker-compose). Команда для
  создания файла:

```bash
echo > .env-non-dev
  ```

* использовать файл docker-compose.yml и команды:

```bash
docker compose build
docker compose up
```

После запуска, приложение будет доступно по адресу: **http://localhost:9001/**

Prometheus будет доступно по адресу **http://localhost:9090/**

Grafana будет доступно по адресу **http://localhost:3000/**

Flower будет доступно по адресу **http://localhost:5555/**

# Конфигурация

## Конфигурация приложения fastAPI

Расположение конфигурационного файла приложения: *app/config/.env*. Данный файл отвечает за конфигурацию fastAPI
приложения.
Содержимое файла *app/config/.env* следующее:

  ```dotenv
MODE=
LOG_LEVEL=
LOGIN_DB=
PASSWORD_DB=
NAME_DB=
HOST=
DB_PORT=
HASH_FUNCTION=
SECRET_KEY=
DIALECT_DB=
DRIVER_DB=

TEST_LOGIN_DB=
TEST_PASSWORD_DB=
TEST_NAME_DB=
TEST_HOST=
TEST_PORT=

SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASS=

HOST_REDIS=
SENTRY_DNS=
  
  ```

Файл заполняется без кавычек. В конце обязательно должна быть пустая строка.

* MODE - режим работы приложения. Доступны следующие варианты: "DEV", "TEST", "PROD"
* LOG_LEVEL - уровень логирования приложения по умолчанию
* LOGIN_DB - логин для базы данных
* PASSWORD_DB - пароль для базы данных
* NAME_DB - имя используемой базы данных
* HOST - хост на котором расположена используемая базы данных
* DB_PORT - порт для подключения на хосте для базы данных
* HASH_FUNCTION - используемая хеш функция для хеширования паролей
* SECRET_KEY - уникальный секретный ключ для jwt токенов
* DIALECT_DB - используемая СУБД. Для выбора возможных вариантов
  ознакомьтесь с [документацией](https://docs.sqlalchemy.org/en/20/core/engines.html)
* DRIVER_DB - драйвер для СУБД. Для выбора возможных вариантов
  ознакомьтесь с [документацией](https://docs.sqlalchemy.org/en/20/core/engines.html)


* TEST_LOGIN_DB - логин тестовой базы данных
* TEST_PASSWORD_DB - пароль тестовой базы данных
* TEST_NAME_DB - имя тестовой базы данных
* TEST_HOST - хост на котором расположена тестовая базы данных
* TEST_PORT - порт для подключения на хосте для тестовой базы данных

* SMTP_HOST - хост SMTP сервиса
* SMTP_PORT - порт SMTP сервиса
* SMTP_USER - пользователь (логин) SMTP сервиса
* SMTP_PASS - пароль SMTP сервиса


* HOST_REDIS - хост расположения redis
* SENTRY_DNS - секретный ключ для сервиса Sentry

## Конфигурация приложения docker compose

Расположение конфигурационного файла docker compose: *.env-non-dev*. Данный файл отвечает за конфигурацию docker
compose.
Содержимое файла следующее:

  ```dotenv
MODE=
LOG_LEVEL=
LOGIN_DB=
PASSWORD_DB=
NAME_DB=
HOST=
DB_PORT=
HASH_FUNCTION=
SECRET_KEY=
DIALECT_DB=
DRIVER_DB=

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=

SMTP_HOST=
SMTP_PORT=
SMTP_USER=
SMTP_PASS=

HOST_REDIS=
SENTRY_DNS=
  
  ```

Переменные все те же, что и в файле *app/config/.env*, за исключением следующих переменных:

* Отсутствуют в *.env-non-dev*:
    * TEST_LOGIN_DB
    * TEST_PASSWORD_DB
    * TEST_NAME_DB
    * TEST_HOST
    * TEST_PORT
* POSTGRES_DB - название базы данных, созданной в docker compose
* POSTGRES_USER - логин базы данных, созданной в docker compose
* POSTGRES_PASSWORD - пароль базы данных, созданной в docker compose

# API Endpoints

### Auth & Пользователи

- `POST /auth/register` - Регистрация нового пользователя.
- `POST /auth/login` - Аутентификация пользователя.
- `POST /auth/logout` - Выход пользователя из системы.
- `GET /auth/me` - Получение данных о текущем пользователе.

### Бронирования

- `GET /bookings` - Получение списка бронирований.
- `POST /bookings/add_booking` - Добавление нового бронирования.
- `DELETE /bookings/{booking_id}` - Удаление бронирования.

### Отели

- `GET /hotels/{location}` - Получение списка отелей по местоположению и датам заезда, выезда.
- `GET /hotels/{hotel_id}/1` - Получение информации об одном отеле.
- `GET /hotels/{hotel_id}/rooms` - Получение списка номеров отеля.

### Фронтенд

- `GET /pages/hotels` - Получение страницы отелей.
- `GET /pages/login` - Получение страницы входа.
- `GET /pages/register` - Получение страницы регистрации.
- `GET /pages/hotels/{location}` - Получение страницы отелей по местоположению.
- `GET /pages/hotels/{hotel_id}/rooms` - Получение страницы номеров отеля.
- `GET /pages/bookings` - Получение страницы бронирований.

### Загрузка картинок

- `POST /images/hotels` - Добавление изображений отеля и номеров.

### Импорт данных в БД

- `POST /import/{table_name}` - Импорт данных в таблицу БД.

### Тестирование Grafana + Prometheus

Данные эндпоинты созданы для проверки Prometheus: создать искусственно ошибки, загрузить память, сделать задержку по
времени

- `GET /prometheus/get_error` - Получение ошибок.
- `GET /prometheus/time_consumer` - Тестирование времени ответа.
- `GET /prometheus/memory_consumer` - Тестирование потребления памяти.

### Default

- `GET /metrics` - Получение метрик.

# Документация API

С документацией приложения, не запуская его, можно ознакомиться по адресу **https://booking-app-73fr.onrender.com/docs**

После запуска приложения документация API будет доступна по адресу **http://localhost:8000/docs.**

# Тестирование

Для удобства запуска тестов созданы файлы:

* `app/tests/run_tests.sh` - для запуска тестов в оболочке Bash
* `app/tests/run_tests.ps1` - для запуска тестов в оболочке PowerShell

Для запуска тестов в Bash выполните команду (находясь в директории Booking-Api):
```bash
app/tests/run_tests.sh
```

Для запуска тестов в PowerShell выполните команду (находясь в директории Booking-Api):
```bash
app/tests/run_tests.ps1
```
