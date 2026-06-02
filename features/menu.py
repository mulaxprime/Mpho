from telegram  import Update 
from telegram.ext import ContextTypes

async def menu(update:Update , context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo ="https://files.catbox.moe/a775ep.jpeg",
        caption ="Mulax Mini Bot \n Support Mulax Prime by joining our channel https://t.me/mulaxprime01 \n Group https://t.me/+HV6CxBLpqgwYzM0 \n Available features: \n /play - search for a song and get the link of the song \n /tts - convert text to speech and send it to you as a voice message \n /chat - ask anything and get a response from the bot"
    )
