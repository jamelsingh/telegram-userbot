from telethon import events
from main import client

# Kick user
@client.on(events.NewMessage(pattern="/kick"))
async def kick_user(event):
    if event.is_group:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            try:
                await event.client.kick_participant(event.chat_id, reply_msg.sender_id)
                await event.reply("✅ User kicked!")
            except Exception as e:
                await event.reply(f"❌ Error: {e}")
        else:
            await event.reply("⚠️ Reply to a user to kick.")
    else:
        await event.reply("❌ This command works only in groups.")

# Promote user (as admin)
@client.on(events.NewMessage(pattern="/promote"))
async def promote_user(event):
    if event.is_group:
        if event.reply_to_msg_id:
            reply_msg = await event.get_reply_message()
            try:
                rights = event.client.types.ChatAdminRights(
                    add_admins=False,
                    invite_users=True,
                    change_info=False,
                    ban_users=True,
                    delete_messages=True,
                    pin_messages=True,
                    manage_call=True
                )
                await event.client.edit_admin(event.chat_id, reply_msg.sender_id, rights, rank="Admin")
                await event.reply("✅ User promoted as admin!")
            except Exception as e:
                await event.reply(f"❌ Error: {e}")
        else:
            await event.reply("⚠️ Reply to a user to promote.")
    else:
        await event.reply("❌ This command works only in groups.")
