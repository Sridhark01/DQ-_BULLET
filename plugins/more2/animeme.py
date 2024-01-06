from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import requests

API_BASE_URL = "https://meme-api.herokuapp.com"


def get_meme(api_endpoint):
    try:
        res = requests.get(f"{API_BASE_URL}/gimme/{api_endpoint}").json()
        return res['url'], res.get('title', 'No Title'), res['postLink']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching meme: {e}")
        return None


def generate_keyboard(callback_data):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Change 🔂",
                    callback_data=callback_data,
                ),
            ],
        ],
    )


@Client.on_message(filters.command(["ameme", "animememe"]))
async def animememes(_, m):
    meme_data = get_meme("animememes")
    if meme_data:
        url, text, link = meme_data
        await m.reply_photo(url, caption=f"[{text}]({link})", reply_markup=generate_keyboard("ameme"))


@Client.on_callback_query(filters.regex("ameme"))
async def ameme(_, query: CallbackQuery):
    meme_data = get_meme("animememes")
    if meme_data:
        query = query.message
        await query.delete()
        url, text, link = meme_data
        await query.reply_photo(url, caption=f"[{text}]({link})", reply_markup=generate_keyboard("ameme"))


                
# ... (Previous code)

@Client.on_message(filters.command("meme"))
async def memes(_, m):
    meme_data = get_meme("memes")
    if meme_data:
        url, text, link = meme_data
        await m.reply_photo(url, caption=f"[{text}]({link})", reply_markup=generate_keyboard("bmeme"))


@Client.on_callback_query(filters.regex("bmeme"))
async def memess(_, query: CallbackQuery):
    meme_data = get_meme("memes")
    if meme_data:
        query = query.message
        await query.delete()
        url, text, link = meme_data
        await query.reply_photo(url, caption=f"[{text}]({link})", reply_markup=generate_keyboard("bmeme"))


@Client.on_message(filters.command(["hmeme", "hentaimeme"]))
async def hetaimemes(_, m):
    meme_data = get_meme("hentaimemes")
    if meme_data:
        url, text, link = meme_data
        await m.reply_photo(url, caption=f"[{text}]({link})", reply_markup=generate_keyboard("cmeme"))


@Client.on_callback_query(filters.regex("cmeme"))
async def hmeme(_, query: CallbackQuery):
    meme_data = get_meme("hentaimemes")
    if meme_data:
        query = query.message
        await query.delete()
        url, text, link = meme_data
        await query.reply_photo(url, caption=f"[{text}]({link})", reply_markup=generate_keyboard("cmeme"))

# ... (Continue with your existing code)

