from abc import ABC, abstractmethod
from template.settings import TEXT_BLOCK, FIELDS_BLOCK, POSTS_LOGS_PATH, COMMENTS_LOGS_PATH
from datetime import datetime
from copy import deepcopy


class MessageTemplate(ABC):
    """
    Класс написан для совместного использования с API слака для
    более простой генерации сообщений бота. Документацию выложу позже.

    """
    to_demonstrate = []

    @abstractmethod
    def compile_message(self):
        """
        Функция должна описывать шаблон наследников этого класса.

        :return:
        """
        pass

    def print_text(self, text: str):
        self.to_demonstrate.append(
            self._insert_into_text_block_of_template(
                TEXT_BLOCK, text
            )
        )

    def divider(self):
        self.to_demonstrate.append(
            {"type": 'divider'}
        )

    def header(self, text):
        template = deepcopy(TEXT_BLOCK)
        template['type'] = 'header'
        template['text']['type'] = 'plain_text'
        template['text']['text'] = text
        self.to_demonstrate.append(
            template
        )

    def show_current_date(self):
        date = f"*{datetime.now().strftime('%d.%m.%Y')}*"
        time = f"*{datetime.now().strftime('%H:%M:%S')}*"

        self.to_demonstrate.append(
            self._insert_into_field_block_of_template(
                FIELDS_BLOCK, ['Сегодня:', date, 'Время на сервере:', time])
        )

    def show_last_n_logs(self, n: int, logs_kind: str) -> tuple:
        logs = self.get_logs(kind=logs_kind)
        text_block_str = " ".join([last_logs_str for last_logs_str in logs[-n:]])
        message = self._insert_into_text_block_of_template(TEXT_BLOCK, text_block_str)
        self.to_demonstrate.append(message)

    def init_payload(self):
        self.generated_message = {
            'channel': self.channel,
            "blocks": self.to_demonstrate
        }

    @staticmethod
    def _insert_into_text_block_of_template(template, text):
        template = deepcopy(template)
        template['text']['text'] = text
        return template

    @staticmethod
    def _insert_into_field_block_of_template(template, text):
        template = deepcopy(template)

        if not isinstance(text, list):
            template['fields']['text'] = text
            return template
        else:
            template['fields'] = [{"type": "mrkdwn", "text": text_str} for text_str in text]
            return template

    @staticmethod
    def get_logs(kind):
        PATH = POSTS_LOGS_PATH if kind == 'posts' else COMMENTS_LOGS_PATH
        with open(PATH, 'r') as fobj:
            return fobj.readlines()


if __name__ == '__main__':
    pass
