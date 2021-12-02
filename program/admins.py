from cache.admins import admins
from driver.veez import call_py, user
from pyrogram import Client, filters
from driver.decorators import authorized_users_only, sudo_users_only
from driver.filters import command, other_filters
from driver.queues import QUEUE, clear_queue
from driver.utils import skip_current_song, skip_item
from config import BOT_USERNAME
from pyrogram.types import Message
from pyrogram.raw.functions.phone import CreateGroupCall
from random import randint


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@sudo_users_only
async def skip(client, m: Message):
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("❌ **Nothing Is Currently Playing !**")
        elif op == 1:
            await m.reply("❗ **Queues is Empty** > `I am Leaving Vc`")
        else:
            await m.reply_text(f"**⏭ Skipped To Next !**\n\n🏷 **Now Playing:** [{op[0]}]({op[1]}.)", disable_web_page_preview= True) 
    else:
        skip = m.text.split(None, 1)[1]
        OP = "🗑 **Removed Track From Queue:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "vstop"])
    & other_filters
)
@sudo_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("✅ **Streaming Ended !**")
        except Exception as e:
            await m.reply(f"🚫 **Error:** `{e}`")
    else:
        await m.reply("❌ **Nothing is Streaming !**")


@Client.on_message(
    command(["pause", f"pause@{BOT_USERNAME}", "vpause"]) & other_filters
)
@sudo_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "⏸ **Paused !**"
            )
        except Exception as e:
            await m.reply(f"🚫 **Error:** `{e}`")
    else:
        await m.reply("❌ **Nothing is Streaming !**")


@Client.on_message(
    command(["resume", f"resume@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "▶️ **Resumed !**"
            )
        except Exception as e:
            await m.reply(f"🚫 **Error:** `{e}`")
    else:
        await m.reply("❌ **Nothing is Streaming !**")


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@sudo_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "🔇 **Muted Myself !**"
            )
        except Exception as e:
            await m.reply(f"🚫 **Error:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nothing is Streaming**")


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@sudo_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "🔊 **Unmuted Myself !"
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nothing is Streaming**")



@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@sudo_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"✅ **Volume Set To** `{range}`%"
            )
        except Exception as e:
            await m.reply(f"🚫 **error:**\n\n`{e}`")
    else:
        await m.reply("❌ **Nothing is Streaming!**")

@Client.on_message(command(["startvc",
                                    "startvc@{USERNAME_BOT"]) & other_filters)
async def startvc(client, m: Message):
    chat_id = m.chat.id
    try:
        await user.send(CreateGroupCall(
            peer=(await user.resolve_peer(chat_id)),
            random_id=randint(10000, 999999999)
        )
        )
        
    except Exception:
        await m.reply(
            "**Error:** My Brain Error `Gib Can manage voice chat` Permission"
        )
