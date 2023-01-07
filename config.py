#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
YOUR_BOT_TOKEN = os.environ.get("YOUR_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Port
PORT = os.environ.get("PORT", "8080")

FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\")
