import asyncio
import logging
from threading import Thread

from core.config import Config
from core import fetcher, filters, database
from bot.telegram_bot import TelegramBot
from server.server import app as server_app

logging.basicConfig(level=logging.INFO)

async def run_bot():
    Config.validate()
    bot = TelegramBot(Config.TELEGRAM_TOKEN, Config.TELEGRAM_CHANNEL)
    database.init_db()

    while True:
        data_sources = [
            fetcher.fetch_data_mevx(),
            fetcher.fetch_data_dexscreener(),
        ]
        all_data = []
        for data in data_sources:
            all_data.extend(data.get("pairs", []) if isinstance(data, dict) else data)

        tokens = filters.filter_tokens(all_data)
        for token in tokens:
            if not database.token_exists(token["pair_address"]):
                msg = f"*{token['base_token']['name']}* launched on {token['dex']}"
                await bot.send_message(msg)
                database.add_token(token["pair_address"])

        await asyncio.sleep(Config.FETCH_INTERVAL)

def run_server():
    server_app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    Thread(target=run_server).start()
    asyncio.run(run_bot())
