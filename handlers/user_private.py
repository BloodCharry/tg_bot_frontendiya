from aiogram import (
    types,
    Router,
    F
)
from aiogram.filters import (CommandStart,
                             Command,
                             or_f,
                             )

from aiogram.enums import ParseMode
from aiogram.utils.formatting import as_list, as_marked_section, Bold
import random

from common import scenarios
from filters.chat_types import CustomChatFilter
from keyboards import reply

user_private_router = Router()
user_private_router.message.filter(CustomChatFilter(['private']))


@user_private_router.message(CommandStart())
async def on_startup(message: types.Message):
    tale = len(scenarios.WELCOME_MESSAGES) - 1
    await message.answer(
        scenarios.WELCOME_MESSAGES[random.randint(0, tale)],
        reply_markup=reply.start_btn.as_markup(
            resize_keyboard=True,
        )
    )


@user_private_router.message(or_f(Command('menu'), (F.text.lower() == "меню \U0001F448")))
async def menu_cmd(message: types.Message):
    # TODO для удаления клавиатуры добавить аргумент reply_markup=reply.del_keyboard
    await message.answer("Вот меню:", reply_markup=reply.menu_btn.as_markup(
        resize_keyboard=True,
    ))


@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("О нас:")


@user_private_router.message(F.text.lower().in_(
    [
        'привет', 'hi', 'хай', 'hello'
    ]
))
async def echo_hello(message: types.Message):
    tale = len(scenarios.WELCOME_MESSAGES) - 1
    await message.answer(scenarios.WELCOME_MESSAGES[
                             random.randint(0, tale)
                         ])


@user_private_router.message(F.text.lower().in_(
    [
        "пока", "bye", "goodbye", "до свидания", "прощай", "до свидания"
    ]
))
async def echo_by(message: types.Message):
    tale = len(scenarios.FAREWELL_MESSAGES) - 1
    await message.answer(scenarios.FAREWELL_MESSAGES[
                             random.randint(0, tale)
                         ])


@user_private_router.message(F.text.lower().in_(
    [
        "как дела", "как у вас дела", "как делишки",
    ]
))
async def echo_how_are_you(message: types.Message):
    tale = len(scenarios.HOW_ARE_YOU_RESPONSES) - 1
    await message.answer(scenarios.HOW_ARE_YOU_RESPONSES[
                             random.randint(0, tale)
                         ])

