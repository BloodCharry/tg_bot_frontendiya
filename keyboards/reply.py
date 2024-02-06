from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='меню'),
            KeyboardButton(text='о нас'),
        ],
        [
            KeyboardButton(text='пробные уроки'),
            KeyboardButton(text='купить курсы'),
        ],
        [
            KeyboardButton(text='Пообщаться'),
        ]

    ],
    resize_keyboard=True,
    input_field_placeholder="Что вас интересует?",
)
