#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @VysakhTG

from pyrogram import Client, filters
from plugins.master.engine import ask_ai


@Client.on_message(filters.command('openai'))
async def openai_ask(client, message):
    if len(message.command) == 1:
       return await message.reply_text("<code> Type Something</code>")
    m = await message.reply_text("👀")
    await ask_ai(client, m, message)
