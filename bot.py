from  telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes  
from features.play import play
from features.tts import tts
from features.menu import menu
from features.chat import chat

TOKEN ="Add_your_telegram_bot_token_here" 
async def start(update, context):
    await update.message.reply_text("Thanks for using Mulax Prime Bot, type /menu to see available features") # the telegram bot must reply to me if the token are working well

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start)) # must add the calling fuction i made 
app.add_handler(CommandHandler("tts",tts)) # must add the calling fuction i made
app.add_handler(CommandHandler("play",play)) # must add the calling fuction i made
app.add_handler(CommandHandler("menu",menu)) #same action too it must display all available features of my bot 
app.add_handler(CommandHandler("chat",chat)) #same action too it must display all available features of my bot 
app.run_polling()   
 
