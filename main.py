
import os
import asyncio
import telegram
from telegram.ext import Updater, CommandHandler
from aiohttp import web
from plugins import web_server
from config import API_HASH, APP_ID, YOUR_BOT_TOKEN, PORT

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            bot_token=YOUR_BOT_TOKEN
        )
def shift_letters(bot, update, args):
  # Get the word and shift amount from the arguments
  word = args[0]
  shift = int(args[1])
  
  # Initialize an empty list to store the modified letters
  modified_letters = []

  # Iterate through each letter in the word
  for letter in word:
    # Shift the letter by the specified number
    modified_letter = chr(ord(letter) + shift)
  
    # Add the modified letter to the list
    modified_letters.append(modified_letter)

  # Join the modified letters together to form the modified word
  modified_word = ''.join(modified_letters)

  # Send the modified word back to the user
  update.message.reply_text(modified_word)

# Create the Updater and attach a handler for the 'shift' command
updater = Updater(bot_token)
updater.dispatcher.add_handler(CommandHandler('shift', shift_letters, pass_args=True))

app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

# Start the bot
updater.start_polling()
