from telethon import events
from main import client

@client.on(events.NewMessage(pattern="/id"))
async def get_id(event):
    await event.reply(f"🆔 Your ID: {event.sender_id}")

@client.on(events.NewMessage(pattern="/info"))
async def user_info(event):
    user = await event.get_sender()
    await event.reply(
        f"📌 Name: {user.first_name}\n"
        f"👤 Username: @{user.username}\n"
        f"🆔 ID: {user.id}"
    )
