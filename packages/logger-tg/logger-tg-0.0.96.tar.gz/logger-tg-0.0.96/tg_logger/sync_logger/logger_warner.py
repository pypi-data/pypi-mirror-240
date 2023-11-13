import requests

from tg_logger.settings import SyncTgLoggerSettings


class ClientLogger:
    def __init__(self, settings: SyncTgLoggerSettings):
        self.bot_token = settings.bot_token
        self.recipient_id = settings.recipient_id
        self.api_url = f'https://api.telegram.org/bot{self.bot_token}/sendMessage'

    def send_error(self, message: str) -> None:
        data = {
            'chat_id': self.recipient_id,
            'text': message
        }
        try:
            response = requests.post(self.api_url, data=data)
            response.raise_for_status()
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")
            return
