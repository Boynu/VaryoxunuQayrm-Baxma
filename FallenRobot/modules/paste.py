import asyncio
import os
import re

import aiofiles
from aiohttp import ClientSession
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton

from FallenRobot import pbot as app
from FallenRobot.utils.errors import capture_err
from FallenRobot.utils.pastebin import paste

pattern = re.compile(r"^text/|json$|yaml$|xml$|toml$|x-sh$|x-shellscript$")


async def isPreviewUp(preview: str) -> bool:
    for _ in range(7):
        try:
            async with ClientSession().head(preview, timeout=2) as resp:
                status = resp.status
                size = resp.content_length
        except asyncio.exceptions.TimeoutError:
            return False
        if status == 404 or (status == 200 and size == 0):
            await asyncio.sleep(0.4)
        else:
            return True if status == 200 else False
    return False


@app.on_message(filters.command("paste"))
@capture_err
async def paste_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("ilə Mesaja Cavab Verin /paste")
    m = await message.reply_text("Yapışdırmaq......")
    if message.reply_to_message.text:
        content = str(message.reply_to_message.text)
    elif message.reply_to_message.document:
        document = message.reply_to_message.document
        if document.file_size > 1048576:
            return await m.edit("Siz yalnız 1MB-dan kiçik faylları yerləşdirə bilərsiniz.")
        if not pattern.search(document.mime_type):
            return await m.edit("Yalnız mətn faylları yapışdırıla bilər.")
        doc = await message.reply_to_message.download()
        async with aiofiles.open(doc, mode="r") as f:
            content = await f.read()
        os.remove(doc)
    link = await paste(content)
    preview = link + "/preview.png"
    button = InlineKeyboard(row_width=1)
    button.add(InlineKeyboardButton(text="Linki yapışdırın", url=link))

    if await isPreviewUp(preview):
        try:
            await message.reply_photo(photo=preview, quote=False, reply_markup=button)
            return await m.delete()
        except Exception:
            pass
    return await m.edit(link)


__mod_name__ = "Pᴀsᴛᴇ"
__help__ = """
Verilmiş faylı yapışdırır və nəticəni sizə göstərir

 ❍ /paste *:* Mətn faylına cavab verin
 """
