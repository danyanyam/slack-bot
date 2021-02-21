from template import MessageTemplate
from template.settings import SLACK_CHANNEL_NAME, LAST_N_LOGS
from slack import WebClient
import os


class SlackBot(MessageTemplate):
    def __init__(self, channel_name_str):
        self.channel = channel_name_str
        self.compile_message()

    def compile_message(self):
        self.print_text(':gear: Краткая статистика по серверу')

        self.divider()
        self.show_current_date()
        self.divider()

        self.header('Парсеры XUEQIU:')
        self.print_text(f'{LAST_N_LOGS} последних лога *постов*:\n\n')
        self.show_last_n_logs(LAST_N_LOGS, 'posts')

        self.print_text(f'\n\n{LAST_N_LOGS} последних лога *комментариев*:\n\n')
        self.show_last_n_logs(LAST_N_LOGS, 'comments')
        self.divider()

        self.init_payload()


if __name__ == '__main__':

    token = os.environ.get("SLACK_TOKEN")
    assert token is not None

    # Устанавливаем связь
    slack_web_client = WebClient(token=token)
    # Инициализируем генератор шаблона сообщений
    bot = SlackBot(SLACK_CHANNEL_NAME)
    # Подготавливаем шаблона
    message = bot.generated_message
    # Отправляем сообщение в слак
    slack_web_client.chat_postMessage(**message)
