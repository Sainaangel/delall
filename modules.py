import os

from pyrogram import Client,filters
from pyrogram.errors import FloodWait,UserAlreadyParticipant,PeerIdInvalid,ChatAdminRequired,ChannelInvalid

import time,json
from pyrogram.types import ChatPrivileges
from config import *


userbot = Client( 'XUserSession', api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)


#--------Commands-----------

@userbot.on_message(filters.command(['start']))
async def start_userbot_cmd(userbot,msg):
	await userbot.send_message(msg.chat.id,'Hello i am Alive')

def get_cht_msg_cmd(bot,msg):
	chat_ID=msg.chat.id
	msg_lis_for_del=[]
	try:
		for message in userbot.get_chat_history(chat_ID):
			msg_lis_for_del.append(message.id)
		return msg_lis_for_del
	except FloodWait as fw:
		bot.send_message(LOG_CHANNEL,fw)
		time.sleep(fw.value)

def send_logs(b,log):
	try:
		b.send_message(LOG_CHANNEL,f'{log}')
	except ChannelInvalid:
		print('Bot is not admin in log channel or channel id invalid')
	except Exception as ex:
		print(ex)

#-------end-of-commands----