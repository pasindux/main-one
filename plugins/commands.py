from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from database.blacklist import check_blacklist
from database.userchats import add_chat
from pyrogram import enums

@Client.on_message(filters.private & filters.command(['start']))
async def start(c:Client, m:Message):
    fuser = m.from_user.id
    if check_blacklist(fuser):
        await m.reply_text("**Sorry! You are Banned!**")
        return
    add_chat(fuser)
    await m.reply_chat_action(enums.ChatAction.TYPING)
    await m.reply_text(
        text=f"**Hey 👋 {m.from_user.mention} Dear! Welcome**\n\n**First you should get an idea about what can this bot upload and what links are supported/how to send links for me by pressing help**",
        reply_markup=InlineKeyboardMarkup([
          [
            InlineKeyboardButton(text="Settings", callback_data="settings") ,
            InlineKeyboardButton(text="Help", callback_data="help")
          ]
        ]),
        quote=True
    )

