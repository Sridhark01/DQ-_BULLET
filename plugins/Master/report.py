from pyrogram import Client, filters, enums

import datetime
import pytz

@Client.on_message((filters.command(["report"]) | filters.regex("@admins") | filters.regex("@admin")) & filters.group)
async def notify_admin(bot, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    administrators = []
    chat_member = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    if (
            chat_member.status == enums.ChatMemberStatus.ADMINISTRATOR
            or chat_member.status == enums.ChatMemberStatus.OWNER
    ):
        return await message.delete()
    async for m in bot.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m)
    full_name = message.from_user.first_name + " " + message.from_user.last_name if message.from_user.last_name else message.from_user.first_name
    
    ist = pytz.timezone("Asia/Kolkata")
    report_time = datetime.datetime.now(pytz.utc).astimezone(ist).strftime("%I:%M:%S %p")
    report_date = datetime.datetime.now(pytz.utc).astimezone(ist).strftime("%d-%B-%Y")
    report_day = datetime.datetime.now(pytz.utc).astimezone(ist).strftime("%A")

    reply_message = f"<b>✅ Report Send Successful ✅\n\n"
    reply_message += f"👤 Rᴇᴘᴏʀᴛᴇᴅ ᴜsᴇʀ: {message.from_user.username}\n"
    reply_message += f"🆔 Rᴇᴘᴏʀᴛᴇᴅ ᴜsᴇʀ ɪᴅ: {message.from_user.id}\n"
    reply_message += f"📝 Rᴇᴘᴏʀᴛ ᴛʀᴀᴄᴋ ɪᴅ: [#TG8836467]({message.link})\n\n"
    reply_message += f"💬 ʀᴇᴘᴏʀᴛ ᴛᴇxᴛ: {message.reply_to_message.text if message.reply_to_message else message.text.split(' ', 1)[1]}\n\n"
    reply_message += f"⏲️ ʀᴇᴘᴏʀᴛ ᴛɪᴍᴇ: {report_time}\n"
    reply_message += f"🗓️ ʀᴇᴘᴏʀᴛ ᴅᴀᴛᴇ: {report_date}\n"
    reply_message += f"⛅ ʀᴇᴘᴏʀᴛ ᴅᴀʏ: {report_day}</b>"

    report = message.reply_to_message if message.reply_to_message else message
    await message.reply_text(reply_message, disable_web_page_preview=True)
    for admin in administrators:
        try:
            if admin.user.id != message.from_user.id:
                await bot.send_message(
                    chat_id=admin.user.id, 
                    text=f"🛠 𝐍𝐞𝐞𝐝 𝐇𝐞𝐥𝐩​!!\n\n<a href=tg://user?id={user_id}>{full_name}</a> Hᴀꜱ Rᴇǫᴜɪʀᴇᴅ Aɴ Aᴅᴍɪɴ Aᴄᴛɪᴏɴ Iɴ Tʜᴇ Gʀᴏᴜᴘ: {message.chat.title}\n\n[➻ 𝖦𝗈 𝖳𝗈 𝖬𝖾𝗌𝗌𝖺𝗀𝖾]({message.link})",
                    disable_web_page_preview=True
                )
        except:
            pass
