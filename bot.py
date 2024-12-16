from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Replace 'your_token_here' with your bot token
BOT_TOKEN = '6948348321:AAH5iX8Sk_uYHkPqpWfzwmft32UVchlAeY4'

# Function that sends "Hi" when /start is triggered
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi")

def main():
    # Create an Application instance
    application = Application.builder().token(BOT_TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Start the bot using long polling
    application.run_polling()

if __name__ == '__main__':
    main()
