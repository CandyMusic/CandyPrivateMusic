
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
đđĄđĸđŦ đđŦ đđđ¯đđ§đđ đĨđđđĨđđ đĢđđĻ đđŽđŦđĸđ đļ đđ¨đ­ \nđđŽđ§ đđ§ đđĢđĸđ¯đđ­đ đĨ đđŠđŦ đĢđđđĢđ¯đđĢ đ \nđđđđĨ â¤ī¸ đđĸđ đĄ đđŽđđĨđĸđ­đ˛ đđŽđŦđĸđ đ§ đđ§ đđ đđ¤ \nâ­đđđ¯đđĨđ¨đŠđđ đđ˛ [ĪÎąÎˇdĪ ÎŠuÎĩÎĩÎˇ](https://t.me/Candy_626)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â°đĨđđđđđđâą", url="https://t.me/Candy_626")
                  ],[
                    InlineKeyboardButton(
                        "â°đĻđđŊđŊđŧđŋđđâą", url="https://t.me/AlishaSupport"
                    ),
                    InlineKeyboardButton(
                        "â°đđŋđŧđđŊđŠâą", url="https://t.me/Shayri_Music_Lovers"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "â°đĨđđĸđđđâą", url="https://t.me/Itz_Venom_xD"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("Esport") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**đđđ§đđ˛ đ­ đđŽđŦđĸđ'đ đđ§đĨđĸđ§đ\nđ ę§āŧē@candy_626āŧģę§ đĨ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "đĻđđŊđŊđŧđŋđâ¤ī¸", url="https://t.me/AlishaSupport")
                ]
            ]
        )
   )
