[![English](https://img.shields.io/badge/lang-en-blue.svg)](README.md)
[![Русский](https://img.shields.io/badge/lang-ru-lightgrey.svg)](README_RU.md)
# MultiBot 🤖✨

MultiBot is a multifunctional Telegram bot: weather, voice messages, photo saving, and instant translation. Built with [aiogram 3.20.0post0](https://docs.aiogram.dev/), it is modular, fast, and easy to extend with new features.

---

## 🚦 Features & Commands

| Command / Action         | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `/start`                | Welcome message.                                                           |
| `/help`                 | Shows this help with all available features.                               |
| `/weather <city>`       | Get current weather for a city: temperature, feels like, condition, humidity, wind, pressure, emoji. |
| `/voice <text>`         | Generate a voice message (TTS, Russian, via gTTS+ffmpeg).                  |
| Send a photo            | The bot saves the largest photo to the `img/` folder on the server.         |
| Send any text (not cmd) | The bot automatically translates any text to English and replies.           |

- Geocoder: uses Yandex first, falls back to OSM Nominatim if no key.
- Fully asynchronous, modular, and easily extensible.
- Docker support, works on Windows and Linux.
- Requires ffmpeg for media/voice features.

---

## 🛠 Stack

* Python ≥3.10 (tested on 3.10 – 3.12)
* aiogram 3.20.0post0
* aiohttp for HTTP
* python‑dotenv for configuration

---

## 🚀 Quick start

```bash
# 1) Clone & enter
$ git clone https://github.com/your‑username/weather_bot.git
$ cd weather_bot

# 2) Virtual env
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

## 🗄 Project Structure

```
main.py                # Entry point, bot startup, router registration
config.py              # Loads and validates environment variables
handlers/
  common.py            # /start, /help
  weather.py           # /weather
  voice.py             # /voice
  media.py             # Photo saving
  translate.py         # Auto-translate any text
utils/
  services.py          # Weather & geocoding (Yandex, OSM)
  formatters.py        # Weather formatting with emoji
  voice.py             # Voice message generation (gTTS + ffmpeg)
  translator.py        # Google Translate API
img/                   # Saved user photos
requirements.txt       # Dependencies
.env                   # Environment variables
```

---

## 📟 Usage Examples

```
/weather Moscow
/voice Hello, how are you?
```
Send a photo — the bot will save it and reply with confirmation.
Send any text — the bot will reply with the English translation.

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

## 🔊 Media & Voice support (FFmpeg)

Some features (voice messages, media conversion) require [FFmpeg](https://ffmpeg.org/):

1. Download FFmpeg from [ffmpeg.org/download](https://ffmpeg.org/download.html).
2. Copy the contents of the `ffmpeg/bin` folder to a directory included in your system `PATH` (e.g., `C:\Windows\System32` on Windows, or `/usr/local/bin` on Linux/Mac).
3. Verify installation by running `ffmpeg -version` in your terminal.

If FFmpeg is not available in `PATH`, media and voice features will not work.

---

## ⚠️ Requirements

- Python 3.10+
- ffmpeg (see below)
- Telegram bot token
- Yandex Weather API key
