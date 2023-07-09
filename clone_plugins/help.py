import time
import random
from pyrogram import Client, filters, enums
from Script import script
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto

CMD = ["/", "."]

ADD_ME = ["https://telegra.ph/file/45991424ebfe111f195e4.jpg",
          "https://telegra.ph/file/8f8cf8d70d38e91a0f4be.jpg",
          "https://telegra.ph/file/3f8ad73dbc9fcf8ae23e7.jpg",
          "https://telegra.ph/file/11cb83b62098072282b30.jpg",
          "https://telegra.ph/file/115f999422a28eecc95cc.jpg",
          "https://telegra.ph/file/3553b5dcc3b12e9ac503c.jpg",
          "https://telegra.ph/file/903f1ca13c4fecc3bf4c9.jpg",
          "https://telegra.ph/file/680f4152c59df899e7c0b.jpg",
          "https://telegra.ph/file/31e53bdab169a8784433b.jpg",
]

@Client.on_message(filters.command(["check"]))
async def help(client, message):
        buttons = [[
            InlineKeyboardButton('FIʟᴛᴇʀs', callback_data='filters'),
            InlineKeyboardButton('Fɪʟᴇ Sᴛᴏʀᴇ', callback_data='store_file')
        ], [
            InlineKeyboardButton('Cᴏɴɴᴇᴄᴛɪᴏɴ', callback_data='coct'),
            InlineKeyboardButton('Exᴛʀᴀ Mᴏᴅs', callback_data='extra')
        ], [
            InlineKeyboardButton('Hᴏᴍᴇ', callback_data='start'),
            InlineKeyboardButton('Sᴛᴀᴛᴜs', callback_data='stats')
        ]]    
        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.send_photo(
           photo=random.choice(ADD_ME),
           caption=script.CHECK_TXT,
           chat_id=message.chat.id,
           reply_markup=reply_markup,
           parse_mode=enums.ParseMode.HTML,
           reply_to_message_id=message.id
       )
