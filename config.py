#-----Config File for Bot-----

import os

try:
	LOG_CHANNEL=int(os.environ.get('LOG_CHANNEL',12))
except:
	LOG_CHANNEL=1234

SESSION_STRING=os.environ.get('SESSION_STRING','')


API_ID=os.environ.get('API_ID','')
API_HASH=os.environ.get('API_HASH','')

BOT_TOKEN=os.environ.get('BOT_TOKEN','')
