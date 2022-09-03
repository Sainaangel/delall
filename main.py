#  Copyright (c) 2022-2023 Thakor Rahul <https://github.com/CrazeBots>
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without
#  limitation the rights to use, copy, modify, merge, publish, distribute 

#Subscribe us YouTube: https://youtube.com/c/TechnologyRk
#Join Telegram: https://t.me/CrazeBots

from modules import *


bot = Client( 'XBotSession', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

#clear terminal by os name
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
clear()


UserBotID=[1]
#start command for bot
@bot.on_message(filters.command(['start','help','delall']))
def start_bot_cmd(bot,msg):
	bot.send_message(msg.chat.id,'**Hello i am Alive**\n\nFor delete all Msgs..\n\n**Use: **`/clearchat` **OR** `/clearall`\n\n**Note:** make sure you added me in your chat with ALL permissions.\nOTHERWISE bot will **NOT** work properly\n\nMade by 🖤 with help of \n**YT: [TechnologyRk](https://youtube.com/c/technologyrk)**')
	ID=userbot.get_me().id
	UserBotID[0]=ID

	
#delete message command, this works only in channel not working for group/supergroups	
@bot.on_message(filters.command(['clearall','clearchat']) & filters.channel)
def delall_bot_cmd(bot,msg):
 msg.reply_text('__Trying to delete MSGs__. \nthis might be take **some time** as depend on Total Msgs in chat..')
 chat_ID=msg.chat.id
 if len(str(UserBotID[0]))<4:
 	msg.delete()
 	msg.reply_text('__Please start me first in private and than use this commad.__')
 	return
 
 #------------Creating_Chat_Link-----#
 
 try:
 	invite_link= bot.create_chat_invite_link(chat_ID)
 	link=json.loads(str(invite_link))
 	link=(link['invite_link'])
 	
 except ChatAdminRequired:
 	text='__Please Allow All Permissions OR then try again !!!__'
 	send_logs(bot,text)
 	return
 
 #---------Joining UserBot--------#
 try:
 	userbot.join_chat(link)
 	time.sleep(2)
 except UserAlreadyParticipant:
 	text='__Something went wrong,\nPlease Run that command again !!!__'
 	send_logs(bot,text)
 	
 #--------Promoting Userbot--------#
 try:
 	bot.promote_chat_member(chat_id=chat_ID,user_id=UserBotID[0],privileges=ChatPrivileges(can_change_info=True,can_delete_messages=True,can_edit_messages=True,can_post_messages=True,can_promote_members=True,can_invite_users=True,can_manage_video_chats=True,is_anonymous=False))
 	
 except ChatAdminRequired:
 	text='__Please Allow All Permissions OR then try again !!!__'
 	send_logs(bot,text)
 	
 except PeerIdInvalid:
 	text='__Please make sure you entered correct user_ID in config file OR then try again !!!__'
 	send_logs(bot,text)
 	
 
 #--------List Of Msgs IDs for Delete----#
 try:
 	msg_ids=get_cht_msg_cmd(userbot,msg)
 	start_time = int(round(time.time()))
 	print('Total MSGs found in chat #: ',len(msg_ids))
 	
 except Exception as Ex3:
 	send_logs(bot,Ex3)
 	return
 
 #-----------Deleting in Loop----------
 for MSG in msg_ids:
 	 
 	 userbot.delete_messages(chat_ID, MSG)
 	 time.sleep(0.08)
 	 
 end_time=int(round(time.time()))
 
 userbot.leave_chat(chat_ID)
 total_time=(end_time-start_time)
 
 text=f'**🔔 Chat : {chat_ID}**\n\n📩 Deleted MSGs : {len(msg_ids)}\n🕰️ Taken Time: {total_time} \n\nThanks for Using me!!\n\n**[Source Code](https://youtube.com/c/technologyrk)**'
 send_logs(bot,text)
	
			
'''
with bot:
	b_data=bot.get_me()
	name=b_data.first_name
	is_bot=b_data.is_bot
	username=b_data.username
	ID=b_data.id
	print(f'\n\nName: {name}\nIs_bot: {is_bot}\nTeleID: {ID}\nUsername: @{username}')
'''


userbot.start()
bot.run()
