import time
import random
import asyncio
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from pyrogram import Client, filters, enums
from info import DLT_TIME
from Script import script
from time import time
from datetime import datetime



async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount} {unit}{"" if amount == 1 else "s"}')
    return ", ".join(parts)

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60**2 * 24),
    ("hour", 60**2),
    ("min", 60),
    ("sec", 1),
)

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    myrr = await message.reply_sticker("CAACAgIAAxkBAAEIK1lkFAN0BjHbiwRY08v-7EFYRqI2fQACKRgAAhP_2UkVxgiD_rlLGS8E")
    andi = await message.reply_text("ʜᴇʏ ʙᴜᴅᴅʏ ɪ ᴀᴍ ᴀʟɪᴠᴇ 💃\n\nᴄʟɪᴄᴋ /start ꜰᴏʀ ᴍᴏʀᴇ​ 😻")
    await asyncio.sleep(DLT_TIME)
    await myrr.delete()
    await andi.delete()
    await message.delete()
    await message.reply_photo(photo=avatar_url, caption=capy, reply_markup=BUTTONS)
    await bot.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
    await k.delete()

@Client.on_message(filters.command("ping", CMD))
async def ping_pong(client, m: Message):
    start = time()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    m_reply = await m.reply_text("Pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        f"🏓 ᴘɪɴɢ: <code>{delta_ping * 1000:.3f}ms</code>\n\n"
        f"⏰ ᴜᴘᴛɪᴍᴇ: <code>{uptime}</code>\n"
    )

@Client.on_message(filters.command("uptime", CMD))
async def get_uptime(client, m: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m.reply_text(
        "ʙᴏᴛ sᴛᴀᴛᴜs\n"
        f"⏰ ᴜᴘᴛɪᴍᴇ: <code>{uptime}</code>\n\n"
        f"sᴛᴀʀᴛ ᴛɪᴍᴇ: <code>{START_TIME_ISO}</code>"
    )
