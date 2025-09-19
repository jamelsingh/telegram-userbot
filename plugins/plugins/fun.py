from telethon import events
from main import client

@client.on(events.NewMessage(pattern="/hello"))
async def hello(event):
    await event.reply("👋 Hello! I am alive.")

@client.on(events.NewMessage(pattern="/joke"))
async def joke(event):
    jokes = [
        "😆 Teacher: Why are you late? Student: Because of the sign on the road. Teacher: What sign? Student: 'School Ahead, Go Slow'!",
        "😂 Patient: Doctor, I feel like a mobile. Doctor: Then why didn’t you call me?",
        "🤣 Boss: You are late again! Employee: Sir, I didn’t sleep well last night. Boss: Then sleep well in office!"
    ]
    import random
    await event.reply(random.choice(jokes))
