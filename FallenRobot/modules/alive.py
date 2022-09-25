import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/911a21ef102ad5a2de3b6.jpg",
    "https://telegra.ph/file/911a21ef102ad5a2de3b6.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ ᴢᴇɴ ✘ ʀᴏʙᴏᴛ​**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **𝗙𝗮𝘁𝗵𝗲𝗿 : [𝗣𝘆𝘁𝗵𝗼𝗻𝗫𝗴𝗮𝗺𝗲𝗿](https://t.me/pythonXgamer)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/zenxrobot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/ViolenceChitChat")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
