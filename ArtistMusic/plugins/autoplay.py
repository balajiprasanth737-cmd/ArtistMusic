# ==========================================================
  # Copyright (c) 2026 ArtistBots
  # All Rights Reserved.
  #
  # Project      : ArtistBots API Telegram Music Bot
  # Powered By   : Artist
  # Type         : API Based Telegram Music Bot
  #
  # Bot          : @ArtistApibot
  # Channel      : https://t.me/artistbots
  # GitHub       : https://github.com/elevenyts/ArtistMusic
  #
  # Unauthorized copying, modification, or redistribution
  # of this source code without permission is prohibited.
  # ==========================================================
from pyrogram import filters, types
from ArtistMusic import app, db
from ArtistMusic.helpers import can_manage_vc

@app.on_message(filters.command(["autoplay", "cautoplay"]) & filters.group)
@can_manage_vc
async def _autoplay(_, m: types.Message):
    try:
        await m.delete()
    except Exception:
        pass

    chat_id = m.chat.id
    current = await db.get_autoplay(chat_id)
    new_state = not current
    await db.set_autoplay(chat_id, new_state)

    if new_state:
        text = (
            "<blockquote>▶ <b>Autoplay: ON</b>\n\n"
            "Autoplay enabled! Continuous playback is active.</blockquote>"
        )
    else:
        text = (
            "<blockquote>⏹ <b>Autoplay: OFF</b>\n\n"
            "Autoplay disabled. Playback will stop when queue ends.</blockquote>"
        )

    await m.reply_text(text)
