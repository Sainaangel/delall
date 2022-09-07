# Channel All Messages Delete Bot [@deleteallbot](https://t.me/crazebots)

> A star ⭐ from you means a lot to us!

<p align="center"><a href="https://www.github.com/CrazeBots/deleteallbot"><img src="https://telegra.ph/file/7ec22c82f580a334dd13e.jpg" width="300" height="300"></a></p>

Telegram bot to Clear OR delete channel messages speedly.

## Usage

### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/CrazeBots/deleteallbot)

1. Tap on above button and fill `API_ID`, `API_HASH`, `BOT_TOKEN` (and `SESSION_STRING`).
2. Then tap "Deploy App" below it. Wait till deploying is complete (will take atmost 1 minute).
3. After deploying is complete, tap on "Manage App"
4. Check the logs to see if your bot is ready!

### Local Deploying

1. Clone the repo
   ```markdown
   git clone https://github.com/CrazeBots/deleteallbot
   ```
   
2. Get a Session String from my.telegram.org
   
3. Edit `config.py` and fill the needed variables

4. Enter the directory
   ```markdown
   cd deleteallbot
   ```
5. Run the file
   ```markdown
   python3 main.py
   ```

## Environment Variables

#### Mandatory Vars

- `API_ID` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `API_HASH` - Get this from [my.telegram.org](https://my.telegram.org/auth)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
- `SESSION_STRING` - Pyrogram Session String for ur userbot.
- `UserBotID` - Username/ID of your pyrogram userbot.
- `OWNERID` - Username/ID of your telegram account.
- `LOG_CHANNEL` - Username/ID of your telegram channel/group.
## Functions

> More features soon if suggested by you :)

1) Delete all messages of channel in 1 commands.
2) Log channel support for if any error occurred.
3) Added Only Owner can use this bot.

## Credits

- [Dan Tès](https://github.com/delivrance) for his [Pyrogram](https://docs.pyrogram.org) Library
- [Aman Sharma](https://t.me/crazebots) for the idea as well as the project logo.

## Support

Channel :- [@CrazeBots](https://t.me/Crazebots)

## :)

[![ForTheBadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://github.com/crazebots)

[![ForTheBadge makes-people-smile](http://ForTheBadge.com/images/badges/makes-people-smile.svg)](https://github.com/Crazebots)
