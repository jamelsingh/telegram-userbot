import os

class Config:
    # Required
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "your_api_hash")
    SESSION = os.environ.get("SESSION", "userbot")

    # Optional
    OWNER_ID = int(os.environ.get("OWNER_ID", 0))  # Owner Telegram ID
    BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID", 0))  # Log group/channel
    DEBUG = bool(os.environ.get("DEBUG", False))
  
