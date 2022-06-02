import logging
import time
import requests
from random import random


from telegram import Update, ForceReply, bot, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Enable logging
from telegram.update import Update
from telegram.inline import inlinekeyboardbutton

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

token = "5341077351:AAEfgbsvk9raSHifg8NS_Km_yYcHP2IVJfU"


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def start(update, context):
    """Send a message when the command/start is issued."""
    update.message.reply_text('Welcome to LinkNUS Bot!\n/help for more information.')



def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('/newTask\t- Add task to a TODO list\n'
                              '/setReminder\t- Set reminder of the task\n'
                              '/getBus\t- Obtain the NUS shuttle bus arrival times\n'
                              '/getZoomLinks\t- Obtain Zoom links of current week lessons\n'
                              '/getDeadlines\t- Get the incoming submission deadlines from LumiNUS\n'
                              '/setDeadlines\t- Set a new deadline/Change a current deadline\n'
                              )
    # Have the reply keyboard over here. [Get Started command]



def getBus(update, context):
    """Get the bus arrival timing at the nearest bus stop."""
    update.message.reply_text('Please type in your nearest bus stop')


def newTask(update, context):
    """Create a new task and add it into the current list of deadlines."""
    # This will give us all the words in the message, which will be something like "/quadratic 1 2 3"
    # all_words = update.message.text.split(" ")
    #
    # # We convert terms from index 1 to 3 to an array of integers
    # terms = list(map(lambda x: int(x), update.message.text.split(" ")[1:]))

    update.message.reply_text('Please type the task name and the deadline in this format(task_dd/mm/yyyy)')


def getZoomLinks(update, context):
    """Get the Zoom links for this week lessons from LumiNUS."""
    # number = int(random() * 100000)
    # url = f"https://cataas.com/cat?id={number}"
    #
    # update.message.reply_photo(photo=url)
    update.message.reply_text('This will return a list of Zoom links with module name')


def getDeadlines(update, context):
    """Get the submission deadlines from LumiNUS."""
    # logger.warning('Update "%s" caused error "%s"', update, context.error)
    update.message.reply_text('This will return a list of the tasks with their deadlines')

def setReminder(update, context):
    """Set a reminder of a task."""
    update.message.reply_text('Please type the task name and the time when you want to be reminded '
                              'in this format(task_1200_dd/mm/yyyy)')

def setDeadlines(update, context):
    """Set a new deadline of some tasks/Change the deadline of some existing tasks"""
    update.message.reply_text('Please type the task name and the new deadline in this format(task_dd/mm/yyyy)')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("getBus", getBus))
    dp.add_handler(CommandHandler("getZoomLinks", getZoomLinks))
    dp.add_handler(CommandHandler("getDeadlines", getDeadlines))
    dp.add_handler(CommandHandler("setDeadlines", setDeadlines))
    dp.add_handler(CommandHandler("newTask", newTask))
    dp.add_handler(CommandHandler("setReminder", setReminder))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()