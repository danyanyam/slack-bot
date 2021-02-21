SLACK_CHANNEL_NAME = 'bots-programmming'

# Путь до логов парсера постов
POSTS_LOGS_PATH = 'xueqiu_posts.log'

# Путь до логов парсера комментариев
COMMENTS_LOGS_PATH = 'xueqiu_comments.log'

# Сколько последних логов показывать
LAST_N_LOGS = 3

# Шаблон текстового блока, отправляемого через API слака
TEXT_BLOCK = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": None,
    },
}

# Шаблон табличного блока, отправляемого через API слака
FIELDS_BLOCK = {
    "type": "section",
    "fields": [
        {
            "type": "mrkdwn",
            "text": ' ',
            "emoji": True
        }
    ]
}
