from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


token = "..."

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام به ربات ما خوش آمدید.")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    if user_text == "سلام":
        await update.message.reply_text("سلام")
    else:
        await update.message.reply_text(f"پیام شما: {user_text}")

def main():
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_text))

    print ("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()