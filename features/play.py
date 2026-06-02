import yt_dlp
from telegram import Update
from telegram.ext import ContextTypes


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    song = " ".join(context.args) # this will join the arguments passed after the command into a single string
    ydl_opts = {"quiet": True, "extract_flat": True}  
    with yt_dlp.YoutubeDL(ydl_opts) as ydl: # this will set the options for yt_dlp
       result = ydl.extract_info(f"ytsearch1:{song}", download=False) # this will get the result of the search
       video = result['entries'][0] # this will get the first video from the result
       title = video['title'] # this will get the title of the video
       link =f"https://www.youtube.com/watch?v={video['id']}" # this will get the link of the video of the song i requsted and it will open youtube if i click the link
    await update.message.reply_text(f"{title}\n{link}")
