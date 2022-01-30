import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAIC_mH1JUrL_s4kgKA5hiDk_Rrl0GYWAAIeCgACz9YRUXNuChP5kGjfIwQ")
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/ffbb096d10dd36ad45337.jpg",
        caption=f"""**━━━━━━━━━━━━ 🌺🌻🌹🌷━━━━━━━━━━
━━━━━━━━━━━━━ 🌺🌻🌹🌷━━━━━━━━━━━━━
😊ʜɪ ɪᴀᴍ ᴛᴇʟᴇɢʀᴀᴍ ᴠᴏɪᴄᴇ ᴍᴜsɪᴄ ʙᴏᴛ... ᴅᴇᴘʟᴏʏ ʙʏ : @santhu_music_bot

┏━━━━━━━━━━━━━━━━━┓ 🌺🌻🌹🌷🌺🌻🌹
┣» ᴏᴘ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ. 
┣» ʜɪɢʜ ǫᴜᴀʟɪᴛʏ  ᴍᴜꜱɪᴄ.
┣» ᴀᴅᴠᴀɴᴄᴇᴅ ꜰᴇᴀᴛᴜʀᴇꜱ.
┣» ꜱᴜᴘᴇʀꜰᴀꜱᴛ ꜱᴘᴇᴇᴅ. 
┣» [𝐃𝐄𝐏𝐋𝐎𝐘 𝐁𝐘 ❤️](https://t.me/santhu_music_bot)
┗━━━━━━━━━━━━━━━━━┛
[𝐎𝐖𝐍𝐄𝐑 ❤️](https://t.me/santhu_music_bot)
𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝐒𝐀𝐍𝐓𝐇𝐔❤️](https://t.me/santhu_music_bot)
━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💞sᴀɴᴛʜᴜ ɴɪ ᴀᴅᴅ ᴄʜᴇsᴜᴋᴏɴᴅɪ💞", url="https://t.me/Santhuadvancefreemusicbot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "☹️ᴏᴡɴᴇʀ😘", url="https://t.me/santhu_music_bot"
                    ),
                    InlineKeyboardButton(
                        "😇ɢʀᴏᴜᴘ💞", url="https://t.me/santhuvc"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "😁ɴᴇᴛᴡᴏʀᴋ😊", url="https://t.me/santhubotupadates"
                    )]
            ]
       ),
    )

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited & ~filters.private)

async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/ffbb096d10dd36ad45337.jpg",
        caption=f"""ᴘʀɪᴠᴀᴛᴇ ʀᴇᴘᴏ !🖤""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💕ᴏᴡɴᴇʀ💕", url=f"https://t.me/santhu_music_bot")
                ]
            ]
        ),
    )

@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Help Menu of 📌sᴀɴᴛʜᴜ 𝐓𝐚𝐠 𝐀𝐥𝐥 𝐁𝐨𝐭**\n\nCommand: @all\n__You can use this command with text what you want to mention others.__\nExample: `@all Good Morning!`\n__You can you this command as a reply to any message. Bot will tag users to that replied messsage__.\n\nFollow [sᴀɴᴛʜᴏsʜ](https://t.me/santhu_music_bot) 𝗢𝗡 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('ᴏᴡɴᴇʀ💞', 'https://t.me/santhu_music_bot'),
        Button.url('ɴᴇᴛᴡᴏʀᴋ📡', 'https://t.me/santhuvc')
      ]
    )
  )
  
@client.on(events.NewMessage(pattern="^@all ?(.*)"))
async def all(event):
  chat_id = event.chat_id
  if event.is_private:
    return await event.respond("__This command Can Be Use In Groups And Channels @santhuvc !__")
  
  is_admin = False
  try:
    partici_ = await client(GetParticipantRequest(
      event.chat_id,
      event.sender_id
    ))
  except UserNotParticipantError:
    is_admin = False
  else:
    if (
      isinstance(
        partici_.participant,
        (
          ChannelParticipantAdmin,
          ChannelParticipantCreator
        )
      )
    ):
      is_admin = True
  if not is_admin:
    return await event.respond("__Only Admins Can Mention All\n\nFor More Go On @santhuvc !__")
  
  if event.pattern_match.group(1) and event.is_reply:
    return await event.respond("__Give me one argument!__")
  elif event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.is_reply:
    mode = "text_on_reply"
    msg = await event.get_reply_message()
    if msg == None:
        return await event.respond("__I Can't Mention Members For Older Messages! (messages which are sent before I'm added to group)__")
  else:
    return await event.respond("__Reply To a Message Or Give Me Some Text To Mention Others\n\nMade bY  [sᴀɴᴛʜᴏsʜ 😇](https://t.me/santhu_music_bot) !__")
  
  spam_chats.append(chat_id)
  usrnum = 0
  usrtxt = ''
  async for usr in client.iter_participants(chat_id):
    if not chat_id in spam_chats:
      break
    usrnum += 1
    usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
    if usrnum == 5:
      if mode == "text_on_cmd":
        txt = f"{usrtxt}\n\n{msg}\n\nMade bY  [sᴀɴᴛʜᴏsʜ 😇](https://ᴛ.ᴍᴇ/santhu_music_bot)"
        await client.send_message(chat_id, txt)
      elif mode == "text_on_reply":
        await msg.reply(usrtxt)
      await asyncio.sleep(2)
      usrnum = 0
      usrtxt = ''
  try:
    spam_chats.remove(chat_id)
  except:
    pass

@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond('__ᴇᴍɪ ʟᴇᴅʜᴜ ʀᴀ ɴɪʙʙᴀ sᴛᴏᴘ ᴄʜᴇʏᴀᴛᴀɴɪᴋɪ...__')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('__ᴄᴀɴᴄᴇʟᴇᴅ ᴍᴇɴᴛɪᴏɴ❌.__')

print(">> 📌sᴀɴᴛʜᴜ 𝐓𝐚𝐠 𝐀𝐥𝐥 𝐁𝐨𝐭 <<")
client.run_until_disconnected()

