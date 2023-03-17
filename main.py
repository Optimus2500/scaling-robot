import telegram
import requests

# Define the Scale AI Spellbook API endpoint and authorization header
SPELLBOOK_API_ENDPOINT = "https://dashboard.scale.com/spellbook/api/v2/deploy/mh42dsb"
SPELLBOOK_API_AUTH_HEADER = {"Authorization": "Basic clfcym14x00cvt11a1e8rtybq"}

# Define the Telegram bot token and create a bot instance
TELEGRAM_BOT_TOKEN = "6269137426:AAGekhhUDqTKwSsGGbZhyKGw_TzK5QdFEmE"
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

def send_to_scale_ai(update, context):
    # Get the text message from the user
    user_text = update.message.text
    
    # Create the input data dictionary for the Scale AI Spellbook API
    input_data = {"input": {"input": user_text}}
    
    # Send a POST request to the Scale AI Spellbook API with the input data and authorization header
    response = requests.post(SPELLBOOK_API_ENDPOINT, json=input_data, headers=SPELLBOOK_API_AUTH_HEADER)
    
    # Get the response JSON from the Scale AI Spellbook API
    response_json = response.json()
    
    # Get the output text from the response JSON and send it back to the user
    output_text = response_json["output"]["output"]
    update.message.reply_text(output_text)

def start(update, context):
    # Send a message to the user when the /start command is received
    update.message.reply_text("Send me some text to get a response from GPT4!")

def help(update, context):
    # Send a message to the user when the /help command is received
    update.message.reply_text("Send me some text to get a response from GPT4!")

# Create an updater and dispatcher for the Telegram bot
updater = telegram.ext.Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add the send_to_scale_ai function as a handler for text messages
dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, send_to_scale_ai))

# Add the start and help functions as handlers for the /start and /help commands
dispatcher.add_handler(telegram.ext.CommandHandler("start", start))
dispatcher.add_handler(telegram.ext.CommandHandler("help", help))

# Start the Telegram bot
updater.start_polling()
