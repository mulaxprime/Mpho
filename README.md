# Mpho: AI Telegram bot with chat, voice, and music

## What is Mpho?

Mpho is a Telegram bot built with a modular architecture, combining AI chat, text-to-speech, and YouTube music search into one assistant. *Mpho* means "gift" in Setswana.

This was my first Python project, where I learned modular architecture, API integration, and async/await, before going on to build Mothusi.

Mpho runs 24/7 on a hosted server, so it's always online.

---

## Try it now

**[Message Mpho on Telegram](https://t.me/MulaxPrimbot)**

No setup needed. Just open the link and start chatting.

---

## Features

- AI chat powered by Groq
- Text-to-speech voice replies via gTTS
- YouTube search and music streaming
- Modular command structure: each feature runs as its own module

---

## Commands

- `/chat <message>`: talk to the AI
- `/play <song name>`: search and stream a song from YouTube
- `/tts <text>`: convert text to a voice message
- `/menu`: see all available commands

---

## Built with

- Python
- python-telegram-bot (Telegram Bot API)
- Groq AI for chat responses
- gTTS for text-to-speech voice replies
- yt-dlp for YouTube search and streaming
- python-dotenv to protect the Groq API key
- Modular architecture with async/await: each feature (chat, play, tts, menu) as its own module

---

## Run it yourself

Want to run your own copy instead of using the hosted bot?

1. Clone the repo
2. Add your Groq API key to `.env` as `GROQ_API_KEY=your_key_here`
3. Run `bot.py`

---

## Developer

**Mulax Prime** (Amantle Mpaekae) | Mogoditshane, Botswana

[GitHub](https://github.com/mulaxprime) · [Portfolio](https://mulaxprime.github.io)
