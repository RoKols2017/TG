[![English](https://img.shields.io/badge/lang-en-blue.svg)](README.md)
[![Русский](https://img.shields.io/badge/lang-ru-lightgrey.svg)](README_ru.md)
# Weather Bot 🤖🌦

Telegram bot that shows real‑time weather for any city using the **Yandex Weather API**. Built with
[aiogram 3.20.0post0](https://docs.aiogram.dev/) and designed as a clean, minimal starter you can extend
with new commands, FSM scenes, keyboards, or other services.

---

## ✨ Features

| ✔️ | Description |
|----|-------------|
| `/weather <city>` | Current weather: temperature, feels‑like, condition, humidity, wind, pressure |
| `/start`, `/help` | Basic onboarding commands |
| Fallback geocoder | Tries **Yandex Geocoder** first; falls back to **OSM Nominatim** if no key |
| Emoji & localisation | Human‑readable Russian output with matching emoji |
| Async HTTP | Fully asynchronous via **aiohttp** |
| Typed, modular code | Easy to debug, test, and extend |

---

## 🛠 Stack

* Python ≥3.10 (tested on 3.10 – 3.12)
* aiogram 3.20.0post0
* aiohttp for HTTP
* python‑dotenv for configuration

---

## 🚀 Quick start

```bash
# 1) Clone & enter
$ git clone https://github.com/your‑username/weather_bot.git
$ cd weather_bot

# 2) Virtual env
$ python -m venv .venv
$ source .venv/bin/activate   # Windows: .venv/Scripts/activate

# 3) Install deps
$ pip install -r requirements.txt

# 4) Configure keys
$ cp .env.example .env
# → paste your Telegram & Yandex keys into .env

# 5) Run the bot
$ python main.py
```

---

## 🔑 Environment variables (`.env`)

| Var | Required | Example | Purpose |
|-----|----------|---------|---------|
| `TOKEN_TG` | ✅ | `123456:ABC-DEF…` | Token from @BotFather |
| `YANDEX_API_KEY` | ✅ | `y0_AQAAA…` | Yandex Weather API key |
| `YANDEX_GEOCODER_KEY` | ❌ | `12345-geo…` | Yandex Geocoder key (paid) |
| `NOMINATIM_USER_AGENT` | ❌ | `weather-bot` | UA string for Nominatim fallback |

If `YANDEX_GEOCODER_KEY` is absent, the bot silently switches to OSM geocoding.

---

## 🗄 Project layout

```
weather_bot/
├── main.py              # entry point & polling loop
├── config.py            # env vars & settings
├── handlers/            # routers per feature
│   ├── common.py        # /start, /help
│   └── weather.py       # /weather command
├── utils/
│   ├── services.py      # Yandex+OSM geocoder & weather fetcher
│   └── formatters.py    # format_weather → pretty output
└── requirements.txt
```

---

## 📟 Usage examples

```
/weather Москва
/weather Berlin
```

Typical reply:
```
🌤 Погода в Москва:
Температура: 15 °C (ощущается как 13 °C)
Состояние: малооблачно
Влажность: 60 %
Ветер: 3 м/с
Давление: 760 мм рт. ст.
```

---

## 🐳 Docker (optional)

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
```

Build & run:
```bash
docker build -t weather-bot .
docker run -d --env-file .env --name weather_bot weather-bot
```

---

## ⚙️ Deployment tips

* **systemd** – simplest for one VPS.
* **Supervisor / PM2** – if you already use them.
* **Heroku / Fly.io / Railway** – add a `Procfile` with `worker: python main.py`.

---

## 🐞 Troubleshooting

| Issue | Fix |
|-------|-----|
| `HTTP 403` on geocoder | Remove `YANDEX_GEOCODER_KEY` to force OSM or ensure your key is valid |
| "Не удалось получить погоду" | Check `YANDEX_API_KEY` or API limits |
| Unicode symbols broken | Set `PYTHONIOENCODING=utf-8` before running |

---

## 📝 License

MIT. Feel free to use and modify.

---

## 🙌 Contributing

PRs are welcome! Please open an issue first to discuss major changes.
