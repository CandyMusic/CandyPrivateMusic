# 🚬 AlishaSupport 🥀 Itz_VeNom_xD ✨

import asyncio

from config import SUDO_USERS

from config import PMPERMIT

from pyrogram import Client

from pyrogram import filters

from pyrogram.types import Message

from callsmusic import client as USER

PMSET =True

pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)

async def pmPermit(client: USER, message: Message):

    if PMPERMIT == "ENABLE":

        if PMSET:

            chat_id = message.chat.id

            if chat_id in pchats:

                return

            await USER.send_message(

                message.chat.id,

                "**𝐇𝐢 𝐆𝐲𝐮𝐬𝐬 :) <𝟑\n𝐀𝐧𝐲 𝐇𝐞𝐥𝐩 𝐃𝐦 𝐌𝐲 𝐒𝐰𝐞𝐞𝐭 💜\n𝐌𝐚𝐬𝐭𝐞𝐫 🎸 :- [❛-𝐌𝐢𝐬𝐬'𝐂𝐚𝐧𝐝𝐲🍬 ](https://t.me/Candy_626) ❤️\n**",

            )

            return

    

@Client.on_message(filters.command(["/pmpermit"]))

async def bye(client: Client, message: Message):

    if message.from_user.id in SUDO_USERS:

        global PMSET

        text = message.text.split(" ", 1)

        queryy = text[1]

        if queryy == "on":

            PMSET = True

            await message.reply_text("**🥀 PM-Permit🤞 Activated ✨ ...**")

            return

        if queryy == "off":

            PMSET = None

            await message.reply_text("**🥀 PM-Permit🤞 De-Activated ✨ ...**")

            return

@USER.on_message(filters.text & filters.private & filters.me)        

async def autopmPermiat(client: USER, message: Message):

    chat_id = message.chat.id

    if not chat_id in pchats:

        pchats.append(chat_id)

        await message.reply_text("**🥀 Auto 🤞 Approved ✨ ...**")

        return

    message.continue_propagation()    

    

@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)

async def pmPermiat(client: USER, message: Message):

    chat_id = message.chat.id

    if not chat_id in pchats:

        pchats.append(chat_id)

        await message.reply_text("**🥀 Approved ✨ ...**")

        return

    message.continue_propagation()    

    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)

async def rmpmPermiat(client: USER, message: Message):

    chat_id = message.chat.id

    if chat_id in pchats:

        pchats.remove(chat_id)

        await message.reply_text("**🥀 Dis-Approved ✨ ...**")

        return

    message.continue_propagation()
