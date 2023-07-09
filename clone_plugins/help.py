import time
import random
from pyrogram import Client, filters, enums
from Script import script
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto

CMD = ["/", "."]

ADD_ME = ["https://telegra.ph/file/5083526feada50efd29dc.jpg",
          "https://telegra.ph/file/a014d59bbc4a3917158d3.jpg",
          "https://telegra.ph/file/0ce3fdbe4369cad5e0113.jpg",
          "https://telegra.ph/file/7c0f6910bd34093983bd9.jpg",
          "https://telegra.ph/file/b4553c00050dec17487e9.jpg",
          "https://telegra.ph/file/720fb80700e0a6451f79a.jpg",
          "https://telegra.ph/file/4c25bfea6ed967ea9f10f.jpg",
          "https://telegra.ph/file/f4869c934a7f2eaa31f79.jpg",
          "https://telegra.ph/file/9f6bfb939571221e1763b.jpg",
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
