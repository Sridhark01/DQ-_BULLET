# Spotify-Downloader

### This download from saavn.me an unofficial api
from pyrogram import Client,filters, enums
import requests,os,wget
# from info import CHAT_GROUP, REQST_CHANNEL, SUPPORT_CHAT_ID, ADMINS

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from info import LOG_CHANNEL, CHNL_LNK
BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('💖🇮🇳✨ Made By ✨🇮🇳💖', url=CHNL_LNK)]])
A = """{} with user id:- {} used /saavn command."""
B = """{} with user id:- {} used /vsaavn command."""

# API = "https://apibu.herokuapp.com/api/y-images?query="

START_MESSAGE = """
𝐇𝐞𝐥𝐥𝐨 <a href='tg://settings'>𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮⚡️</a>
<i>📌ഏതു സോങ് ആണോ വേണ്ടത് അത് സ്പെല്ലിങ് തെറ്റാതെ ഗ്രൂപ്പിൽ ചോദിച്ചാൽ മാത്രമേ കിട്ടുകയുള്ളു...!! \n\n

𝐑𝐮𝐥𝐞𝐬 𝐀𝐧𝐝 𝐁𝐨𝐭 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬


𝐅𝐨𝐫 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 :-
/ssong 𝐀𝐥𝐨𝐧𝐞✔️ =-= 𝐬𝐚𝐚𝐯𝐧 𝐦𝐩𝟑 𝐬𝐨𝐧𝐠
/svideo 𝐀𝐥𝐨𝐧𝐞✔️ =-= 𝐬𝐚𝐚𝐯𝐧 𝐦𝐩𝟒 𝐬𝐨𝐧𝐠
/ysong 𝐀𝐥𝐨𝐧𝐞✔️ =-= 𝐲𝐨𝐮𝐭𝐮𝐛𝐞 𝐦𝐩𝟑 𝐬𝐨𝐧𝐠
/yvideo 𝐀𝐥𝐨𝐧𝐞✔️ =-= 𝐲𝐨𝐮𝐭𝐮𝐛𝐞 𝐦𝐩𝟒 𝐬𝐨𝐧𝐠

/𝐬𝐚𝐚𝐯𝐧 𝐀𝐥𝐨𝐧𝐞 𝐄𝐧𝐠𝐥𝐢𝐬𝐡 ❌️
/𝐯𝐦𝐩𝟒 𝐀𝐥𝐨𝐧𝐞 𝐔𝐧𝐝𝐨❌️
/𝐲𝐬𝐨𝐧𝐠 𝐀𝐥𝐨𝐧𝐞 𝐒𝐨𝐧𝐠❌️
/𝐲𝐯𝐢𝐝𝐞𝐨 𝐀𝐥𝐨𝐧𝐞 𝐍𝐞𝐰❌️

𝐌𝐝𝐢𝐬𝐤 𝐋𝐢𝐧𝐤 𝐂𝐨𝐧𝐯𝐞𝐫𝐭𝐞𝐫
𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐀𝐧𝐝 𝐓𝐲𝐩𝐞 /𝐦 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐌𝐝𝐢𝐬𝐤 𝐋𝐢𝐧𝐤
𝐎𝐰𝐧𝐞𝐫 𝐍𝐚𝐦𝐞 :- {}
𝐆𝐫𝐨𝐮𝐩 𝐍𝐚𝐦𝐞 :- {}
"""







@Client.on_message(filters.command('svideo') & filters.text)
async def video(client, message): 
    try:
       args = message.text.split(None, 1)[1]
    except:
        return await message.reply("/svideo requires an argument.")
    if args.startswith(" "):
        await message.reply("/svideo requires an argument.")
        return ""
    pak = await message.reply('Downloading...')
    try:
        r = requests.get(f"https://saavn.me/search/songs?query={args}&page=1&limit=1").json()
    except Exception as e:
        await pak.edit(str(e))
        return
    r = requests.get(f"https://saavn.me/search/songs?query={args}&page=2&limit=2").json()
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
#   album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp3", "mp4")
    os.rename(file, ffile)
    buttons = [[
        InlineKeyboardButton("JOIN MOVIES", url=CHNL_LNK)
    ]]                           
    await message.reply_video(
    video=ffile, caption=f"[{sname}]({r['data']['results'][0]['url']}) - from @RE_X_BOTZ ",thumb=thumbnail,
    reply_markup=InlineKeyboardMarkup(buttons)
)
    await message.reply_text(text="download mp3 song @RE_X_BOTZ")
    os.remove(ffile)
    os.remove(thumbnail)
    await pak.delete()

    await client.send_message(LOG_CHANNEL, B.format(message.from_user.mention, message.from_user.id)) 
    


#    await client.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
        

@Client.on_message(filters.command('ssong') & filters.text)
async def song(client, message):
    try:
       args = message.text.split(None, 1)[1]
    except:
        return await message.reply("/ssong requires an argument.")
    if args.startswith(" "):
        await message.reply("/ssong requires an argument.")
        return ""
    pak = await message.reply('Downloading...')
    try:
        r = requests.get(f"https://saavn.me/search/songs?query={args}&page=1&limit=1").json()
    except Exception as e:
        await pak.edit(str(e))
        return
    sname = r['data']['results'][0]['name']
    slink = r['data']['results'][0]['downloadUrl'][4]['link']
    ssingers = r['data']['results'][0]['primaryArtists']
  #  album_id = r.json()[0]["albumid"]
    img = r['data']['results'][0]['image'][2]['link']
    thumbnail = wget.download(img)
    file = wget.download(slink)
    ffile = file.replace("mp4", "mp3")
    os.rename(file, ffile)
    await pak.edit('Uploading...')
    await message.reply_audio(audio=ffile, title=sname, performer=ssingers,caption=f"[{sname}]({r['data']['results'][0]['url']}) - from saavn ",thumb=thumbnail)
    os.remove(ffile)
    os.remove(thumbnail)
    await pak.delete()
    await client.send_message(LOG_CHANNEL, A.format(message.from_user.mention, message.from_user.id)) 
    

@Client.on_message(filters.command("song") & filters.group) 
async def r_message(client, message):
    mention = message.from_user.mention
    buttons = [[
        InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'https://t.me/RE_X_BOTZ')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(START_MESSAGE.format(message.from_user.mention, message.chat.title),
    protect_content=True,
    reply_markup=reply_markup, 
    parse_mode=enums.ParseMode.HTML
    )
