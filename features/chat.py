from telegram import Update
from telegram.ext import ContextTypes
from  groq import Groq
import os 
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = " ".join(context.args)  
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query}
        ]
    )
    answer = response.choices[0].message.content
    await update.message.reply_text(answer)
