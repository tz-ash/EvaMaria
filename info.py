import re
from os import environ
id_pattern = re.compile(r'^.\d+$')


# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/4958c274b93f606d6a78c.jpg https://telegra.ph/file/124fc9548157e422e717c.jpg https://telegra.ph/file/203c0e6c9c0a581c54b01.jpg https://telegra.ph/file/cf5e306310062668794e2.jpg https://telegra.ph/file/9e35a32090dd0ebde3d0b.jpg https://telegra.ph/file/a729d153ebe397ca1911c.jpg https://telegra.ph/file/582cf3fca0dd1e5e22151.jpg https://telegra.ph/file/615bc23fe67d85c91bee6.jpg https://telegra.ph/file/ad7684ad2ed9f64dfc4c4.jpg https://telegra.ph/file/a351a48a1baee7dd5f75f.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')

CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
