import aiohttp
import logging

class TelegramBot:
    def __init__(self, token, channel):
        self.token = token
        self.channel = channel

    async def send_message(self, text):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {"chat_id": self.channel, "text": text, "parse_mode": "Markdown"}
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data) as resp:
                    if resp.status != 200:
                        logging.warning(f"Failed to send message: {await resp.text()}")
        except Exception:
            logging.exception("Error sending Telegram message")
