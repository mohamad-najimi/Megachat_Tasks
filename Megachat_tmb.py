from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters


token = "..."



def main():
    app = ApplicationBuilder().token(token).build()


    print ("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()