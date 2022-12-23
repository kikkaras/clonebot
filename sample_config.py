#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "25031360"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "b6e73b921948a2f437d19bc2c2aaa595")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AQAjp51Ylxd_5PlQ1o99gxMwdK3hIe71_YA65Ia5qFM-iewGvRxGzqsR1v0oB4hM1PojpM-UQpNdB-NWWssgVVZf2orew0R5X1gRKRIMZxTwFeq91jqd6Z5NeCmgV5S9sJ7MKnyiVDmy7TlU2IG0vwQvBcD5MQAo9Yzezs3gRj5be_5Nk5bKmKG-G3E1H4XBIB4uAixoiN-zQkL6x-2Jvvmdp1EBxPzBHFJxakNl_1gwMwz6VWtrre_gfruRld1RXducshgrydpYqj2A09nqcaZGKEpqvlCvf1TI-NYcPMg6X3qfTstPi7RkDRQUduXfrmh9Jt0hQMXm9cTssmOAYZYZAAAAATvpR2AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgresql://dipon:amithnajanaja333@localhost:5432/cluster100")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
