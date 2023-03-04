from pyrogram import filters
from pyrogram.types import Message

from strings import get_command
from AmangMusic import app
from AmangMusic.misc import SUDOERS
from AmangMusic.utils.database.memorydatabase import (
    get_active_chats, get_active_video_chats)
from AmangMusic import userbot

# Commands
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")


@app.on_message(filters.command(ACTIVEVC_COMMAND, [".", "-", "!", "^", "/"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text(
        "Getting active voice chats.. Please hold"
    )
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "Private Group"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("No Active Voice Chats")
    else:
        await mystic.edit_text(
            f"**Active Voice Chats:-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(ACTIVEVIDEO_COMMAND, [".", "-", "!", "^", "/"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text(
        "Getting active video chats.. Please hold"
    )
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "Private Group"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("No Active Voice Chats")
    else:
        await mystic.edit_text(
            f"**Active Video Calls:-**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command("active", [".", "^", "-", "!", "/"]) & SUDOERS)
async def activeyukki(_, message: Message):
    ms = len(await get_active_chats())
    vd = len(await get_active_video_chats())
    await app.send_message(message.chat.id, 
        f"🫵 **Active Chats:**\n\n• **Music:** `{ms}`\n• **Stream:** `{vd}`")

    
@app.on_message(filters.command("samlekom", [".", "(", "-", "!", "/"]) & SUDOERS)
async def asshimiko(_, message: Message):
    await userbot.one.send_message(message.chat.id, "**ASSISTANT 1 AKTIF BANH**")
    await userbot.two.send_message(message.chat.id, "**ASSISTANT 2 JUGA AKTIF BOS**")
    await userbot.three.send_message(message.chat.id, "**GILIRAN AKU KAH?**")
    await userbot.four.send_message(message.chat.id, "**MAAF, KETIDURAN BANH**")
    await userbot.five.send_message(message.chat.id, "**TETEP HADIR WALAU TERAKHIR**")
