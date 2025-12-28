from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


token = "..."

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام به ربات ما خوش آمدید.")

def main():
    app = ApplicationBuilder().token(token).build()
    
    app.add_handler(CommandHandler("start", start_command))


    print ("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()