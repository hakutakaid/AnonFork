# Copyright (C) 2024 by DemusIndonesia @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall, GroupCallNotFound

import config
from config import BANNED_USERS
from HakutakaMusic import LOGGER, app, userbot
from HakutakaMusic.core.call import Alexa
from HakutakaMusic.misc import sudo
from HakutakaMusic.plugins import ALL_MODULES
from HakutakaMusic.utils.database import get_banned_users, get_gbanned


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("HakutakaMusic").error("Add Pyrogram string session and then try...")
        sys.exit()
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
        importlib.import_module("HakutakaMusic.plugins" + all_module)
    LOGGER("HakutakaMusic.plugins").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await Alexa.start()
    try:
        await Alexa.stream_call("https://telegra.ph/file/b60b80ccb06f7a48f68b5.mp4")
    except (NoActiveGroupCall, GroupCallNotFound):
        LOGGER("HakutakaMusic").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        sys.exit()
    except:
        pass
    await Alexa.decorators()
    LOGGER("HakutakaMusic").info("Alexa Music Bot Started Successfully")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("HakutakaMusic").info("Stopping Alexa Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
    LOGGER("HakutakaMusic").info("Stopping Music Bot")
