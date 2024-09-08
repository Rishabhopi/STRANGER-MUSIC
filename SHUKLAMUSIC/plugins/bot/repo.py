from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SHUKLAMUSIC import app
from config import BOT_USERNAME

start_txt = """❖ ʜᴇʏ , ᴛʜᴇʀᴇ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ  ♥︎

➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 ➲ ɴᴏ ɪssᴜᴇ ✰
 ➲ ɴᴏ ʙᴀɴ ɪssᴜᴇ ✰
 ➲ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 ► Iғ ʏᴏᴜ ᴡᴀɴᴛ ʀᴇᴘᴏ ᴛʜᴀɴ ᴅᴍ ᴍʏ ᴏᴡɴᴇʀ"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/NenoBots"),
          InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/Rishu1286")
          ],
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://envs.sh/bJh.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
