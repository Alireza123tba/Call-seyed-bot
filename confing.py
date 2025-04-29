import os

class Config:
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")
    MIN_MARKET_CAP = int(os.getenv("MIN_MARKET_CAP", 60000))
    MIN_VOLUME_24H = int(os.getenv("MIN_VOLUME_24H", 100000))
    MAX_AGE_MINUTES = int(os.getenv("MAX_AGE_MINUTES",160))
    TARGET_DEX = os.getenv("TARGET_DEX", "Uniswap","pumpfun")
    FETCH_INTERVAL = int(os.getenv("FETCH_INTERVAL", 180))

    @staticmethod
    def validate():
        assert Config.TELEGRAM_TOKEN, "TELEGRAM_TOKEN is required"
        assert Config.TELEGRAM_CHANNEL, "TELEGRAM_CHANNEL is required"
