import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 21973813))
    API_HASH = os.environ.get("API_HASH", "c578b64ac7af52f363f9e0ebfbc67923")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5880556247:AAG0Q4bf_ZUXY-n36_za2vkx0bcV-x27OW0")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1001930933230))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "iPopcorn_Movie_Bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 5313004751))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Rishikesh001:Rishikesh001@cluster0.lqncnak.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://youtube.com/@GreyMattersBot'>Link Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""

