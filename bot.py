from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8756162788:AAEnQjBUgt646MDkJvFfUyLGMqQwRtQ_2Sc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hii 👋")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
