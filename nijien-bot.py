from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start_bot(update,context):
    # Your bot will send this message when users first talk to bot 
    #using /start command
    update.message.reply_text('Hi! Welcome. Please give me any text and i will echo it for you')

def need_help(update, context):     
   # on /help command
   update.message.reply_text('Help!')

def echo(update, context):     
   update.message.reply_text(update.message.text)

def main():
    updater = Updater('6085880765:AAGuXjlelVSx0b4hin0lzcYozR-yLVPkvQ4')
    
    #get dispatcher from updater to register handlers
    dp = updater.dispatcher
    
    # adding start command handler to dispatcher.
    #handles /start command      
    dp.add_handler(CommandHandler('start',start_bot))
    # calls help method on /help command
    dp.add_handler(CommandHandler('help',need_help))
    #on noncommand i.e for text other than start and help , echo    
    #the message on Telegram        
    dp.add_handler(MessageHandler(Filters.text, echo))
    
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives     
    #SIGINT, SIGTERM or SIGABRT. This should be used most of the      
    # time, since,start_polling() is non-blocking and will stop 
    # the bot
    updater.idle() 
  
if __name__ == '__main__':
    main()