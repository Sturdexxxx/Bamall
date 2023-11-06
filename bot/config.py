import os
from os import getenv

class Config:
    TELEGRAM_TOKEN = getenv("6152349862:AAHgp4yWPAWkZJzooe8h0SF32wKQpXNl05Q", None)
    PYRO_SESSION = getenv("PYRO_SESSION", None)
    TELEGRAM_APP_HASH= getenv('10e3ed833b0d09699973420d45359409')
    TELEGRAM_APP_ID=int(getenv('4665778'))
        
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
    if not TELEGRAM_TOKEN or not PYRO_SESSION:
        raise ValueError("PYRO_SESSION / TELEGRAM_TOKEN not set")
