import functools

import requests
from pyrogram import filters

from Yuriko.function.pluginhelpers import get_text
from Yuriko import pbot

API1 = "https://single-developers.up.railway.app/logo?name="
API2 = "https://single-developers.up.railway.app/logohq?name="


def is_admin(func):
    @functools.wraps(func)
    async def oops(client, message):
        is_admin = False
        try:
            user = await message.chat.get_member(message.from_user.id)
            admin_strings = ("creator", "administrator")
            if user.status not in admin_strings:
                is_admin = False
            else:
                is_admin = True

        except ValueError:
            is_admin = True
        if is_admin:
            await func(client, message)
        else:
            await message.reply("**Only Admins can execute this command!**")

    return oops


@pbot.on_message(filters.command("slogo") & ~filters.edited & ~filters.bot)
async def logo_maker(client, message):
    if message.reply_to_message:
        try:
            msg = await client.send_message(
                message.chat.id, "**Creating The Logo....**"
            )
        except:
            return
        try:
            text = get_text(message.reply_to_message)
        except:
            return
        if (
            message.reply_to_message.video
            or message.reply_to_message.document
            or message.reply_to_message.photo
            or message.reply_to_message.animation
            or message.reply_to_message.sticker
        ):
            try:
                await msg.edit("Sorry I can't get the text of replied message")
                return
            except:
                return
        if not text:
            try:
                await msg.edit("**Invalid Command Syntax**\n\n`/logo [name]`")
                return
            except:
                return
        try:
            req = requests.get(API1 + text.replace(" ", "%20"))
        except:
            return
        try:
            url = req.history[1].url
        except:
            return
        try:
            await msg.delete()
        except:
            return
        try:
            await message.reply_photo(
                url,
                caption=f"**Logo Generated Successfully** As {text}\n\nImage Link => {url}\n\n**By @Mr_Shadow_Robot**",
            )
        except:
            return

    else:
        try:
            msg = await client.send_message(
                message.chat.id, "**Creating The Logo....**"
            )
        except:
            return
        try:
            text = get_text(message)
        except:
            return
        if not text:
            try:
                await msg.edit("**Invalid Command Syntax**\n\n`/logo [name]`")
                return
            except:
                return
        try:
            req = requests.get(API1 + text.replace(" ", "%20"))
        except:
            return
        try:
            url = req.history[1].url
        except:
            return
        try:
            await msg.delete()
        except:
            return
        try:
            await message.reply_photo(
                url,
                caption=f"**Logo Generated Successfully** As {text}\n\nImage Link => {url}\n\n**By 𝙆𝙄𝙂𝙊**",
            )
        except:
            return


@pbot.on_message(filters.command("logohq") & ~filters.edited & ~filters.bot)
async def logohq(client, message):
    if message.reply_to_message:
        try:
            msg = await client.send_message(
                message.chat.id, "**Creating The Logo....**"
            )
        except:
            return
        try:
            text = get_text(message.reply_to_message)
        except:
            return
        if (
            message.reply_to_message.video
            or message.reply_to_message.document
            or message.reply_to_message.photo
            or message.reply_to_message.animation
            or message.reply_to_message.sticker
        ):
            try:
                await msg.edit("Sorry I can't get the text of replied message")
                return
            except:
                return
        if not text:
            try:
                await msg.edit("**Invalid Command Syntax**\n\n`/logo [name]`")
                return
            except:
                return
        try:
            req = requests.get(API2 + text.replace(" ", "%20"))
        except:
            return
        try:
            url = req.history[1].url
        except:
            return
        try:
            await msg.delete()
        except:
            return
        try:
            await message.reply_photo(
                url,
                caption=f"**Logo Generated Successfully** As {text}\n\nImage Link => {url}\n\n**By 𝙆𝙄𝙂𝙊**",
            )
        except:
            return

    else:
        try:
            msg = await client.send_message(
                message.chat.id, "**Creating The Logo....**"
            )
        except:
            return
        try:
            text = get_text(message)
        except:
            return
        if not text:
            try:
                await msg.edit("**Invalid Command Syntax**\n\n`/logo [name]`")
                return
            except:
                return
        try:
            req = requests.get(API2 + text.replace(" ", "%20"))
        except:
            return
        try:
            url = req.history[1].url
        except:
            return
        try:
            await msg.delete()
        except:
            return
        try:
            await message.reply_photo(
                url,
                caption=f"**Logo Generated Successfully** As {text}\n\nImage Link => {url}\n\n**By 𝙆𝙄𝙂𝙊**",
            )
        except:
            return


__mod_name__ = "LᴏɢᴏMᴀᴋᴇʀ"

__help__ = """

✗ /logo - `<text/name> Create a logo with your name`

✗ /logo Null ; Robot :  use ; for write in next line

✗ /slogo - `<text/name> Create a simple logo with random view.`

✗ /wlogo - `<text/name> Create a logo with wide view only.`

✗ /slogo - `<text/name> Create a simple  wide view logo.`

 *Image Editor :*

✗  /edit - `<reply photo> to edit image.`

**✗ Pᴏᴡᴇʀᴇᴅ 🔥 Bʏ: Kɪɢᴏ Dᴜɴɪʏᴀ**

"""
