import os
import shutil
from pyrogram import Client, filters, enums
from telegraph import upload_file
from plugins.helpers.get_file_id import get_file_id
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

TMP_DOWNLOAD_DIRECTORY = "./DOWNLOADS/"

@Client.on_message(
    filters.command("telegraph") 
)
async def telegraph(client, message):
    koshik = await message.reply_text("**Processing...😪**")
    replied = message.reply_to_message
    if not replied:
        await koshik.edit_text("Reply to a supported media file")
        return
    file_info = get_file_id(replied)
    if not file_info:
        await koshik.edit_text("Not supported!")
        return
    _t = os.path.join(
        TMP_DOWNLOAD_DIRECTORY,
        str(replied.id)
    )
    if not os.path.isdir(_t):
        os.makedirs(_t)
    _t += "/"
    download_location = await replied.download(
        _t
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await koshik.edit_text(message, text=document)
    else:
        await koshik.edit_text(            
            text=f"<b>Link :-</b> <code>https://telegra.ph{response[0]}</code>\n\n<b>",
            parse_mode=enums.ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    '🎭 ⭕️ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ⭕️', url=f'https://t.me/RE_X_BOTZ'
                                )
                            ]
                        ]
                    )
                )
    finally:
        shutil.rmtree(
            _t,
            ignore_errors=True
        )

@Client.on_message(filters.command("tg_txt"))
async def txt(client, message: Message):
    reply = message.reply_to_message

    if not reply or not reply.text:
        return await message.reply("Reply to a text message")

    if len(message.command) < 2:
        return await message.reply("**Usage:**\n /tg_txt [Page name]")

    page_name = message.text.split(None, 1)[1]
    page = client.create_page(
        page_name, html_content=(reply.text.html).replace("\n", "<br>")
    )
    return await message.reply(
        f"**Posted:** {page['url']}",reply_markup=InlineKeyboardMarkup([ 
        [InlineKeyboardButton('View 💫' , url=f"{page['url']}")]
    ]),disable_web_page_preview=True,
    )
