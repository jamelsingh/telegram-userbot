import os
from telethon import TelegramClient, events

# Values from Environment Variables
API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", "your_api_hash")
SESSION = os.environ.get("SESSION", "userbot")

client = TelegramClient(SESSION, API_ID, API_HASH)

# Auto load plugins
def load_plugins():
    for plugin in os.listdir("plugins"):
        if plugin.endswith(".py") and plugin != "__init__.py":
            try:
                imported = __import__(f"plugins.{plugin[:-3]}")
                print(f"✅ Loaded Plugin - {plugin}")
            except Exception as e:
                print(f"❌ Error loading {plugin}: {e}")

@client.on(events.NewMessage(pattern="/ping"))
async def ping(event):
    await event.reply("🏓 Pong!")

if __name__ == "__main__":
    load_plugins()
    print("🚀 Userbot Started...")
    client.start()
    client.run_until_disconnected()
