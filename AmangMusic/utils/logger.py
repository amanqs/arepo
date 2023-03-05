#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from config import LOG, LOG_GROUP_ID
from AmangMusic import app
from AmangMusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"
        logger_text = f"""
• **ᴀᴍᴀɴɢ ʟᴏɢɢᴇʀ**

————————
• **ɢʀᴏᴜᴘ»** {message.chat.title} 
• ** ɪᴅ ɢʀᴏᴜᴘ»** [`{message.chat.id}`]
• **ʟɪɴᴋ»** {chatusername}
• **ɴᴀᴍᴀ»** {message.from_user.mention}
• **ᴜsᴇʀɴᴀᴍᴇ»** @{message.from_user.username}
• **ɪᴅ ᴘᴇɴɢɢᴜɴᴀ»** `{message.from_user.id}`
—————————

• **ᴘᴇɴᴄᴀʀɪᴀɴ»** {message.text}
• ** sᴛʀᴇᴀᴍ ᴛʏᴘᴇ»** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
