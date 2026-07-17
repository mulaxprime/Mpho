from gtts import gTTS
from telegram import Update
from telegram.ext import ContextTypes
import os 

async def tts(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    text = " ".join(context.args) # this must allow  my arguements  join the arguments passed after the command into a single string
    tts = gTTS(text)
    tts.save("voice.mp3") # this will save the audio file as voice.mp3
    await update.message.reply_voice(voice=open("voice.mp3", "rb")) # this will send the audio file to the user
    os.remove("voice.mp3") # this will delete the audio file after sending it to the user
