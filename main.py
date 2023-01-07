import telegram
from telegram.ext import Updater, CommandHandler

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
updater = Updater(YOUR_BOT_TOKEN)
updater.dispatcher.add_handler(CommandHandler('shift', shift_letters, pass_args=True))

# Start the bot
updater.start_polling()