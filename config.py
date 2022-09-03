#-----Config File for Bot-----

from os import environ


OWNERID=int(environ.get('OWNERID'))
UserBotID=int(environ.get('UserBotID'))
LOG_CHANNEL=environ.get('LOG_CHANNEL')

SESSION_STRING=environ.get('SESSION_STRING')


API_ID=int(environ.get('API_ID'))
API_HASH=environ.get('API_HASH')

BOT_TOKEN=environ.get('BOT_TOKEN')