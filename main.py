from pyrogram import Client, filters

# Replace with your API ID and API Hash from my.telegram.org
API_ID = "YOUR_API_ID"
API_HASH = "YOUR_API_HASH"

# The name of your session (creates a session file)
SESSION_NAME = "telegram_forwarder"

# Source group/channel (replace with the source chat ID or username)
SOURCE_CHAT_ID = "source_group_or_channel"

# List of target groups/channels (replace with target chat IDs or usernames)
TARGET_CHAT_IDS = ["target_group_or_channel_1", "target_group_or_channel_2"]

# Initialize the Pyrogram client
app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.chat(SOURCE_CHAT_ID))
async def forward_message(client, message):
    for target_chat in TARGET_CHAT_IDS:
        try:
            await message.forward(target_chat)
            print(f"Forwarded message to {target_chat}")
        except Exception as e:
            print(f"Failed to forward message to {target_chat}: {e}")

if __name__ == "__main__":
    print("Starting Telegram Auto-Forwarder...")
    app.run()
