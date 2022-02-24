from telegram.ext import Updater, CommandHandler


def start(update, context):
    update.message.reply_text('Hello World! ❤')

def bye(update, context):
    update.message.reply_text('See you next time! 👋')


if __name__ == '__main__':
    token = '5274743215:AAFNrjUxdYgpaQeDF0pumbMVIwORYVxEyEY'
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('bye', bye))

    # add handler
    updater.start_polling()
    updater.idle()