[![English](https://img.shields.io/badge/lang-en-lightgrey.svg)](README.md)
[![Русский](https://img.shields.io/badge/lang-ru-blue.svg)](README_ru.md)
# Weather Bot 🤖🌦

Телеграм‑бот, который показывает актуальную погоду для любого города, используя **API Яндекс.Погоды**. Построен на
[aiogram 3.20.0post0](https://docs.aiogram.dev/ru/) и служит аккуратным стартовым проектом, который легко расширить
новыми командами, сценами FSM, клавиатурами или другими сервисами.

---

## ✨ Возможности

| ✔️ | Что делает |
|----|------------|
| `/weather <город>` | Текущая погода: температура, ощущается как, состояние, влажность, ветер, давление |
| `/start`, `/help` | Базовые команды‑подсказки |
| Резервный геокодер | Сначала **Яндекс Геокодер**, при ошибке — **OSM Nominatim** |
| Эмодзи и русский текст | Дружелюбный русскоязычный вывод с подходящими emoji |
| Async HTTP | Полностью асинхронный через **aiohttp** |
| Типизированный, модульный код | Проще отлаживать, тестировать и дорабатывать |

---

## 🛠 Стек

* Python ≥3.10 (проверено на 3.10 – 3.12)
* aiogram 3.20.0post0
* aiohttp для HTTP
* python‑dotenv для конфигурации

---

## 🚀 Быстрый старт

```bash
# 1) Клонируем и заходим
$ git clone https://github.com/your‑username/weather_bot.git
$ cd weather_bot

# 2) Виртуальное окружение
$ python -m venv .venv
$ source .venv/bin/activate   # Windows: .venv/Scripts/activate

# 3) Ставим зависимости
$ pip install -r requirements.txt

# 4) Создаём .env и вносим ключи
$ cp .env.example .env
# → вставьте токен Telegram и ключ Яндекс.Погоды

# 5) Запускаем бота
$ python main.py
```

---

## 🔑 Переменные окружения (`.env`)

| Переменная | Обязательна | Пример | Назначение |
|------------|-------------|--------|------------|
| `TOKEN_TG` | ✅ | `123456:ABC-DEF…` | Токен из @BotFather |
| `YANDEX_API_KEY` | ✅ | `y0_AQAAA…` | Ключ API Яндекс.Погоды |
| `YANDEX_GEOCODER_KEY` | ❌ | `12345-geo…` | Ключ Яндекс.Геокодера (платный) |
| `NOMINATIM_USER_AGENT` | ❌ | `weather-bot` | UA‑строка для Nominatim‑fallback |

Если `YANDEX_GEOCODER_KEY` не задан, бот автоматически переключится на OSM.

---

## 🗄 Структура проекта

```
weather_bot/
├── main.py              # вход и цикл polling
├── config.py            # переменные окружения
├── handlers/            # роутеры по фичам
│   ├── common.py        # /start, /help
│   └── weather.py       # /weather
├── utils/
│   ├── services.py      # геокодер + погода
│   └── formatters.py    # человекочитаемый вывод
└── requirements.txt
```

---

## 📟 Примеры использования

```
/weather Москва
/weather Berlin
```

Типичный ответ:
```
🌤 Погода в Москва:
Температура: 15 °C (ощущается как 13 °C)
Состояние: малооблачно
Влажность: 60 %
Ветер: 3 м/с
Давление: 760 мм рт. ст.
```

---

## 🐳 Docker (опционально)

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
```

Сборка и запуск:
```bash
docker build -t weather-bot .
docker run -d --env-file .env --name weather_bot weather-bot
```

---

## ⚙️ Советы по деплою

* **systemd** — самое простое на одном VPS.
* **Supervisor / PM2** — если уже используете.
* **Heroku / Fly.io / Railway** — добавьте `Procfile` с `worker: python main.py`.

---

## 🐞 Решение проблем

| Проблема | Решение |
|----------|---------|
| `HTTP 403` от геокодера | Удалите `YANDEX_GEOCODER_KEY`, чтобы форсировать OSM, или проверьте ключ |
| «Не удалось получить погоду» | Проверьте `YANDEX_API_KEY` и лимиты API |
| Крякозябры в выводе | Запустите с `PYTHONIOENCODING=utf-8` |

---

## 📝 Лицензия

MIT. Используйте и модифицируйте свободно.

---

## 🙌 Вклад

PR ‑ы приветствуются! Перед крупными изменениями откройте issue для обсуждения.
