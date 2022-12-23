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
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5690182894:AAGJ0hHFck5cMpvusG1PKbhgQ-t0nWv0ZSk")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "25031360"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "b6e73b921948a2f437d19bc2c2aaa595")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "AQARqLeO2MscpiEIRoMiIXcZ4LT1yLXeVYNqJP_O5yivvGpyCgqDogYOAnlMEt001ETuCTQ0ZEURHnnxF57TmIfGvrvohd9ODyYU7dyGdjoH40FOC_T8sMS_EL6VaADC3jVfNZ0tNiXURqWWmeRIsEmnDXUxABZ4X53sA51YgXU5RIVqpiUjnndgRFAyyvyvdAa1W5-SGOztd9zJ7pPT3e3idMfmpnbFkcLMkLv3vieGZjPdAAYgbL9pcdBY50A1hiAi8QiFuiPgpXFp53SjEYrKTocMNXEWYWD3qDaJCrc5u4tuB7x_GvcI0CdsYH3kBP_aRVXNjKjjasKxt9V9mVX_AAAAATvpR2AA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgresql://dipon:amithnajanaja333@localhost:5432/cluster100")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
