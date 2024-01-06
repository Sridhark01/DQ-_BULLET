from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters
import requests

# These codes were created by @lallu_tgs

@Client.on_message(filters.command(["ameme", "animememe"]))
async def animememes(_, m):
    try:
        res = requests.get("https://meme-api.herokuapp.com/gimme/animememes").json()
        url = res['url']
        text = res.get('title', 'No Title')
        link = res['postLink']
        
        await m.reply_photo(url, caption=f"[{text}]({link})", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="ameme",
                    ),
                ],
            ],
        ))
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching anime meme: {e}")
        # Handle the error, log it, or take appropriate action.
        await m.reply_text("Sorry, an error occurred while fetching the anime meme. Please try again later.")


@Client.on_callback_query(filters.regex("ameme"))
async def ameme(_, query: CallbackQuery):
                   query = query.message
                   await query.delete()
                   res = requests.get("https://meme-api.herokuapp.com/gimme/animememes").json()
                   url = res['url']
                   text = res['title']
                   link = res['postLink']
                   await query.reply_photo(url,caption=f"[{text}]({link})",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="ameme",
                    ),
                ],
            ],
        ),
    )
                
@Client.on_message(filters.command("meme"))
async def memes(_, m):
     res = requests.get("https://meme-api.herokuapp.com/gimme/memes").json()
     url = res['url']
     text = res['title']
     link = res['postLink']
     await m.reply_photo(url,caption=f"[{text}]({link})",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="bmeme",
                    ),
                ],
            ],
        ),
    )
        
@Client.on_callback_query(filters.regex("bmeme"))
async def memess(_, query: CallbackQuery):
                   query = query.message
                   await query.delete()
                   res = requests.get("https://meme-api.herokuapp.com/gimme/memes").json()
                   url = res['url']
                   text = res['title']
                   link = res['postLink']
                   await query.reply_photo(url,caption=f"[{text}]({link})",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="bmeme",
                    ),
                ],
            ],
        ),
    )

@Client.on_message(filters.command(["hmeme","hentaimeme"]))
async def hetaimemes(_, m):
     res = requests.get("https://meme-api.herokuapp.com/gimme/hentaimemes").json()
     url = res['url']
     text = res['title']
     link = res['postLink']
     await m.reply_photo(url,caption=f"[{text}]({link})",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="cmeme",
                    ),
                ],
            ],
        ),
    )
        
@Client.on_callback_query(filters.regex("cmeme"))
async def hmeme(_, query: CallbackQuery):
                   query = query.message
                   await query.delete()
                   res = requests.get("https://meme-api.herokuapp.com/gimme/hentaimemes").json()
                   url = res['url']
                   text = res['title']
                   link = res['postLink']
                   await query.reply_photo(url,caption=f"[{text}]({link})",reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Change 🔂",
                        callback_data="cmeme",
                    ),
                ],
            ],
        ),
    )
