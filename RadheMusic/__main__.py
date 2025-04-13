
import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from RadheMusic import LOGGER, app, userbot
from RadheMusic.core.call import RadheMusic
from RadheMusic.misc import sudo
from RadheMusic.plugins import ALL_MODULES
from RadheMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from RadheMusic.plugins.tools.clone import restart_bots


async def init():
    if not config.STRING1:
        LOGGER(__name__).error("String Session not filled, please provide a valid session.")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("RadheMusic.plugins" + all_module)
    LOGGER("RadheMusic.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await RadheMusic.start()
    try:
        await RadheMusic.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("RadheMusic").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        exit()
    except:
        pass
    await RadheMusic.decorators()
    await restart_bots()
    LOGGER("RadheMusic").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝗔𝗔𝗥𝗩𝗜☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("RadheMusic").info("𝗦𝗧𝗢𝗣 𝗔𝗔𝗥𝗩𝗜 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
