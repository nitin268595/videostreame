import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "dlwrml")
ALIVE_NAME = getenv("ALIVE_NAME", "Blaze")
BOT_USERNAME = getenv("BOT_USERNAME", "veezvideobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "cleo_invida")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "VeezSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "levinachannel")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "900"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d45664925769e7cea64a9.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6798d34159854b48bfc52.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/61937ce89397da402d82c.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/8ee0bc857c6d60977d769.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/78284abac2d5c43e6a18a.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d7c44036672092af79d48.jpg")
IMG_7 = getenv("IMG_7", "CAACAgUAAxkBAAED2ZBiAQn3kQ51pAleWgABHkgcHExJhl0AAlQEAAIbZQlUudoxEzNMjfgjBA")
