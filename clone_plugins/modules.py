import time
import random
from pyrogram import Client, filters, enums
from Script import script
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto

CMD = ["/", "."]

@Client.on_message(filters.command(["rules"]))
async def help(client, message):
        buttons = [[
                    InlineKeyboardButton('𝚁𝚄𝙻𝙴𝚂', callback_data="rule"),
                  ]]
        
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.send_photo(
           photo="https://telegra.ph/file/255fbc98b0ea8d7646826.jpg",
           caption=script.RULES_TXT,
           chat_id=message.chat.id,
           reply_markup=reply_markup,
           parse_mode=enums.ParseMode.HTML,
           reply_to_message_id=message.id
       )

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
        await client.send_text(
           text=script.CHECK_TXT,
           chat_id=message.chat.id,
           reply_markup=reply_markup,
           parse_mode=enums.ParseMode.HTML,
           reply_to_message_id=message.id
       )
