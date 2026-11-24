import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    secret = os.environ.get("MY_SECRET_MESSAGE", "не задана")
    return f"""
    <!doctype html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Flask в облаке</title>
        <style>
            body {{ font-family: Arial, sans-serif; max-width: 760px; margin: 12vh auto;
                   padding: 24px; background: #f3f7fb; color: #183247; }}
            main {{ background: white; padding: 32px; border-radius: 16px;
                    box-shadow: 0 8px 28px #18324718; }}
            h1 {{ color: #176b91; }}
            code {{ background: #eaf2f7; padding: 4px 8px; border-radius: 5px; }}
        </style>
    </head>
    <body><main>
        <h1>Приложение работает в облаке!</h1>
        <p>Flask-приложение успешно запущено. CI/CD проверен!</p>
        <p>Переменная окружения <code>MY_SECRET_MESSAGE</code>:
           <strong>{secret}</strong></p>
    </main></body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
