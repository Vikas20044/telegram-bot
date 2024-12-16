from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    # Send a "Hi" message to the user
    update.message.reply_text('Hi!')

def main():
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    token = 'YOUR_BOT_TOKEN'
    
    # Create the Updater and pass the bot's token
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler('start', start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
