# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'
BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'

# Bot settings
MAX_RESULTS = 10
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [12345789, 'admin123', 98765432]
CHANNELS = [-10012345678, -100987654321, 'channelusername']
AUTH_USERS = []

# MongoDB information
DATABASE_URI = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb]?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

# Messages
START_MSG = """
**Hola, soy el bot de búsqueda de archivos de Pro Android :D**

Aquí puede buscar archivos en inline mode. Simplemente presione los siguientes botones y comience a buscar aplicaciones subidas al canal de Pro Android © (específicamente, del canal @baseddatos)

**Bot creado y gestionado por @DKzippO, si quieres conocer mis canales visita @CanalesFamosos :D**
"""

SHARE_BUTTON_TEXT = 'Revisa {username} para buscar archivos de Pro Android :D'
