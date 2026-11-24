# Flask Cloud Deployment

Учебный проект для практической работы по развёртыванию Python-приложения на Render.

## Локальный запуск

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Откройте http://127.0.0.1:5000

## Настройка Render

Создайте Web Service и подключите GitHub-репозиторий.

- Runtime: Python 3
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

В разделе Environment добавьте:
- Key: `MY_SECRET_MESSAGE`
- Value: `hello-cloud`

Render самостоятельно задаёт переменную `PORT`. Приложение также поддерживает локальный запуск на порту 5000.

## Проверка

- Главная страница: `/`
- Проверка состояния: `/health` (возвращает JSON `{"status": "ok"}`)

Не помещайте реальные пароли, токены и API-ключи в исходный код или Git.
