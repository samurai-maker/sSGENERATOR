from pyrogram import filters

from bot.screenshotbot import ScreenShotBot
from bot.config import Config


HELP_TEXT = """
Hi {mention}. <code>Welcome to Screenshot Generator Bot. You can use me to generate:

    1. Screenshots.
    2. Sample Video.
    3. Trim Video.

👉 I support any kind of **telegram video file** (streaming video or document video files) provided it --has proper mime-type-- and --is not corrupted--.
👉 I also support **Streaming URLs**. The URL should be a --streaming URL--, --non IP specific--, and --should return proper response codes--.
Just send me the telegram file or the streaming URL.</code>

<b>See /settings to configure bot's behavior.
Use /set_watermark to set custom watermarks to your screenshots.</b>

<b>**General FAQ.** <b>
<code>
👉 If the bot dosen't respond to telegram files you forward, first check</code><b> /start and </b><code>--confirm bot is alive--. Then make sure the file is a **video file** which satisfies above mentioned conditions.
👉 If bot replies __😟 Sorry! I cannot open the file.__, the file might be --currupted-- or --is malformatted--.
</code>
__If issues persists contact <b>@world_wide_movies</b>.__

{admin_notification}
"""
ADMIN_NOTIFICATION_TEXT = (
    "Since you are one of the admins, you can check /admin to view the admin commands."
)


@ScreenShotBot.on_message(filters.private & filters.command("help"))
async def help_(c, m):

    await m.reply_text(
        text=HELP_TEXT.format(
            mention=m.from_user.mention,
            admin_notification=ADMIN_NOTIFICATION_TEXT
            if m.from_user.id in Config.AUTH_USERS
            else "",
        ),
        quote=True,
    )
