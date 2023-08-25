import sys
from pyrogram import Client, filters, enums
from pyrogram.types import *
from info import ADMINS
from utils import humanbytes  
import requests
import io
#import time
import traceback
from requests import post
from subprocess import getoutput as run
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


def paste(text):
    url = "https://spaceb.in/api/v1/documents/"
    res = post(url, data={"content": text, "extension": "txt"})
    return f"https://spaceb.in/{res.json()['payload']['id']}"

@Client.on_message(filters.user(ADMINS) & filters.command("sh", prefixes=['/', '.', '?', '-']) & filters.private)
def sh(_, m: Message):
    try:
        code = m.text.replace(m.text.split(" ")[0], "")
        x = run(code)
        m.reply(
              f"<code>SHELL: {code}\n\nOUTPUT:\n{x}</code>")
        x = paste(x)
        m.reply("7.4.0" + x)
    except Exception as e :
        pass
        x = paste(x)
        h = m.reply(x)
        m.reply(e)

@Client.on_message(filters.user(ADMINS) & filters.command("eval"))
async def eval(client, message):
    status_message = await message.reply_text("Processing ...")
    cmd = message.text.split(" ", maxsplit=1)[1]

    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"

    final_output = "<b>EVAL</b>: "
    final_output += f"<code>{cmd}</code>\n\n"
    final_output += "<b>OUTPUT</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code> \n"

    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await reply_to_.reply_document(
                document=out_file, caption=cmd, disable_notification=True
            )
    else:
        await reply_to_.reply_text(final_output)
    await status_message.delete()

async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)
@Client.on_message(
    filters.command("linklogs", prefixes=[".", "/", ";", "," "*"]) & filters.user(ADMINS)
)
def sendlogs(_, m: Message):
    logs = run("tail bot.log")
    x = paste(logs)
    keyb = [
        [
            InlineKeyboardButton("Link", url=x),
            InlineKeyboardButton("File", callback_data="sendfile"),
        ],
    ]
    m.reply(x, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(keyb))
