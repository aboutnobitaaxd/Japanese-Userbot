# COPYRIGHT (C) 2024 BY NOBITA_XD
"""
(((((((((((((((((((((((@Nobitaa_xd)))))))))))))))))))))))))))
(((((((((((((((((((((((@Nobitaa_xd)))))))))))))))))))))))))))
(((((((((((((((((((((((@Nobitaa_xd)))))))))))))))))))))))))))
(((((((((((((((((((((((@Nobitaa_xd)))))))))))))))))))))))))))
"""
# MADE BY NOBITA_XD🔥
# 
import asyncio
import os
try:
  from pyrogram import Client, idle
except:
  os.system("pip install pyrogram>=1.1.13")
  from pyrogram import Client, idle

import asyncio
from userbot.utils import admin_cmd as legendx
from userbot import bot as NOBITA_XD
API_ID = os.environ.get("APP_ID", None)
API_HASH = os.environ.get("API_HASH", None)
from telethon import events, custom, Button, TelegramClient
import time
from userbot import botnickname, ALIVE_NAME, bot
token = os.environ.get("TG_BOT_TOKEN_BF_HER", None)
xbot = TelegramClient("NOBITA_XD", API_ID, API_HASH).start(bot_token=token)
pbot = Client("NOBITA_XD", api_id=API_ID, api_hash=API_HASH, bot_token=token)
BOT = str(botnickname) if botnickname else "JAPANESE BOT"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "NOBITA_XD"
PHOTO = os.environ.get("ALIVE_PHOTTO", None)
NOBITA_XD= "[NOBITA_XD](https://t.me/Nobitaa_xd)"
VERSION = "3.1.5"
ID = 6694740726
REPO = "[Japanese Bot](https://github.com/nobitaaxd/Japanese-Userbot-.git)"
PRO = bot.uid
MASTER = f"[{NAME}](tg://user?id={PRO})"
GROUP = "[SUPPORT GROUP](https://t.me/Japanese_Userbot_Chat)"
if name=="main":
  xbot.run_until_disconnected()

if name=="main":
  pbot.start()
  run()
