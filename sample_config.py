# Just change the info below and rename this file to config.py

from pyrogram import filters

API_ID = 1725988
API_HASH = "35b829bed9b38bb0a5e8079e777277cf"
TOKEN = "1416304053:AAFkAx7Fr4A0V3ZkySAbzGPEwkh5Hj-WMgc"
SUDO_USERS = [
    695291232,
    919584113,
    1153786300
]
LOG_GROUP = None # Just keep it like this if you are not going to use one

# No need to touch this
SUDO_FILTER = filters.user(SUDO_USERS)
