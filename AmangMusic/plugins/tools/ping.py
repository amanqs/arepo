#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from AmangMusic import app
from AmangMusic.core.call import Amang
from AmangMusic.utils import bot_sys_stats
from AmangMusic.utils.decorators.language import language
from AmangMusic.misc import SUDOERS

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Amang.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            MUSIC_BOT_NAME, resp, UP, DISK, CPU, RAM, pytgping
        )
    )
    
@app.on_message(filters.command("usage", [".", "(", "-", "!", "/"]) & SUDOERS)
async def usageamang(_, message: Message):
    await app.send_message(message.chat.id,
        f" ❂ **Music Usage **:\n\n"
        f" » Dyno usage for **amangmusic**:\n"
        f" •  `17`**h**  `24`**m** "
        f"\n\n  » Dynos heroku {UP} days left"
    )
