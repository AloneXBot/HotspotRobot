import secureme
from HotspotRobot.events import register


@register(pattern="^/encrypt ?(.*)")
async def encrypt(event):
    if event.reply_to_msg_id:
        lel = await event.get_reply_message()
        cmd = lel.text
    else:
        cmd = event.text.split(" ", 1)
        if len(cmd) == 1:
            await event.reply(f"**Usage:**\n - /encrypt <ᴛᴇxᴛ>\n - /encrypt <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>")
            return
        cmd = cmd[1]

    k = secureme.encrypt(cmd)
    await event.reply(k)


@register(pattern="^/decrypt ?(.*)")
async def decrypt(event):
    if event.reply_to_msg_id:
        lel = await event.get_reply_message()
        ok = lel.text
    else:
        ok = event.text.split(" ", 1)
        if len(ok) == 1:
            await event.reply(f"**Usage:**\n - /decrypt <ᴛᴇxᴛ>\n - /decrypt <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>")
            return
        ok = ok[1]

    k = secureme.decrypt(ok)
    await event.reply(k)

__mod_name__ = "Tᴏᴏʟs"

__help__ = """
𝗖𝗼𝗻𝘃𝗲𝗿𝘁𝘀:
  ➲ /encrypt: ᴇɴᴄʀʏᴘᴛꜱ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
  ➲ /decrypt: ᴅᴇᴄʀʏᴘᴛꜱ ᴘʀᴇᴠɪᴏᴜꜱʟʏ ᴇᴄʀʏᴘᴛᴇᴅ ᴛᴇxᴛ
"""
