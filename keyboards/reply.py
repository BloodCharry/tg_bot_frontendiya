from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)

from aiogram.utils.keyboard import ReplyKeyboardBuilder


start_btn = ReplyKeyboardBuilder()
start_btn.add(
    KeyboardButton(text='меню \U0001F448'),
    KeyboardButton(text='о нас \U0001F609'),
    KeyboardButton(text='пробные уроки \U0001F58B'),
    KeyboardButton(text='купить курсы \U0001F911', ),
    KeyboardButton(text='Пообщаться \U0001F4AC'),
)
start_btn.adjust(2, 2, 1)

menu_btn = ReplyKeyboardBuilder()
menu_btn.add(
    KeyboardButton(text='Первый пункт'),
    KeyboardButton(text='Второй пункт'),
    KeyboardButton(text='Трейтий пункт'),
)
menu_btn.adjust(1, 1, 1)

new_menu_btn = ReplyKeyboardBuilder()
new_menu_btn.attach(menu_btn)
new_menu_btn.row(KeyboardButton(text='Оставить отзыв'))
# del_keyboard = ReplyKeyboardRemove()
