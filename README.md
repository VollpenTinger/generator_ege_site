# Генератор вариантов ЕГЭ по математике

Веб-приложение на Django для автоматической генерации уникальных вариантов заданий по математике (профильный уровень ЕГЭ)

![Python](https://img.shields.io/badge/Python-3.12.10-blue)
![Django](https://img.shields.io/badge/Django-5.2.8-green)
![Postgres](https://img.shields.io/badge/PostgreSQL-14-blue)
![Docker](https://img.shields.io/badge/Docker-ready-blue)

## Возможности
- Генерация случайных вариантов из большой базы задач   
- Удобный веб-интерфейс  
- Полностью контейнеризировано (Docker + Docker Compose)

## Быстрый старт (Docker Compose)

### 1. Клонируйте репозиторий💿
```bash
git clone https://github.com/yourusername/generator-ege-site.git
cd generator-ege-site
```

### 2. Создайте файл .env⚙️ 
```
bash .env.example .env
```
Отредактируйте .env при необходимости (для разработки можно оставить как есть)

### 3. Запуск в режиме разработки (с hot-reload) 🚀 
```
bash docker-compose -f docker-compose.dev.yml up --build
```

### 4. Примените миграции и создайте суперюзера🐦
```
bash docker-compose exec web python manage.py migrate
```
```
bash docker-compose exec web python manage.py createsuperuser
```
### 5. Готово✅