from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'your_token_here' with your bot token
BOT_TOKEN = '6948348321:AAH5iX8Sk_uYHkPqpWfzwmft32UVchlAeY4'

# Function that sends "Hi" when /start is triggered
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hi")

def main():
    # Initialize the Updater with your bot's token
    updater = Updater(token=BOT_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the /start command handler
    dp.add_handler(CommandHandler("start", start))

    # Start the bot using long polling
    updater.start_polling()

    # Keep the bot running until interrupted
    updater.idle()

if __name__ == '__main__':
    main()
