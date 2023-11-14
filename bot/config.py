from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 22611165))
    API_HASH = env.get("TELEGRAM_API_HASH", "3bbecf69a234f3c3852bc23c2a04cc86")
    OWNER_ID = int(env.get("OWNER_ID", 5196029054))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "sukuna_stream_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6964781767:AAEhRPoU4SuAFqxCbKpL7VotQT_VZk9jsv4")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002100360843))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "http://20.9.174.104:8080")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
