# Mpho — AI Telegram Bot with Chat, Voice, and Music

## What is Mpho?
Mpho is a Telegram bot built with a modular architecture, combining AI chat, text-to-speech, and YouTube music search into one assistant. *Mpho* means "gift" in Setswana.

This was my first Python project — where I learned modular architecture, API integration, and async/await, before going on to build Mothusi.

---

## Features
- AI chat powered by Groq
- Text-to-speech voice replies via gTTS
- YouTube search and music streaming
- Modular command structure — each feature runs as its own module

---

## Built With
- Python
- python-telegram-bot (Telegram Bot API)
- Groq AI — chat responses
- gTTS — text-to-speech voice replies
- yt-dlp — YouTube search and streaming
- python-dotenv — protects the Groq API key
- Modular architecture with async/await — each feature (chat, play, tts, menu) as its own module

---

## How to Use
Mpho currently runs locally — the bot is only online while my PC is running it. To try it yourself:
1. Clone the repo
2. Add your Groq API key to `.env` as `GROQ_API_KEY=your_key_here`
3. Run `bot.py`

---

## Commands
- `/chat <message>` — talk to the AI
- `/play <song name>` — search and stream a song from YouTube
- `/tts <text>` — convert text to a voice message
- `/menu` — see all available commands

---

## live demo
[Telegram](https://t.me/MulaxPrimbot)

## Developer
**Mulax Prime** (Amantle Mpaekae) | Mogoditshane, Botswana
[GitHub](https://github.com/mulaxprime) · [Portfolio](https://mulaxprime.github.io)
