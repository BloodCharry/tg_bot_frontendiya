from aiogram import (
    types,
    Router,
    F,
)
from aiogram.filters import (CommandStart,
                             Command,
                             or_f,
                             )

from aiogram.enums import ParseMode
from aiogram.utils.formatting import as_list, as_marked_section, Bold
from aiogram.types import InputFile
import random

from common import scenarios
from filters.chat_types import ChatTypeFilter
from keyboards import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))




@user_private_router.message(CommandStart())
async def on_startup(message: types.Message):
    tale = len(scenarios.WELCOME_MESSAGES) - 1
    await message.answer(
        scenarios.WELCOME_MESSAGES[random.randint(0, tale)],
        reply_markup=reply.get_keyboard(
            "Бесплатные материалы",
            "Часто задаваемые вопросы",
            "Хочу записаться к вам на мок-бес",
            placeholder="Что вас интересует?",
            sizes=(1, 1, 1)
        )
    )


@user_private_router.message(F.text == "Бесплатные материалы")
async def free_materials(message: types.Message):
    # TODO для удаления клавиатуры добавить аргумент reply_markup=reply.del_keyboard
    await message.answer("выберите один из пунктов", reply_markup=reply.get_keyboard(
        "Гайд по настройке eslint/prettier/husky/vite",
        "Frontend roadmap для начинающих",
        placeholder="Выберите один из пунктов",
        sizes=(1, 1)
    )
    )

@user_private_router.message(F.text == "Часто задаваемые вопросы")
async def faq(message: types.Message):
    await message.answer("выберите один из пунктов", reply_markup=reply.get_keyboard(
        "Как проходит менторство?",
        "Как происходит оплата",
        "Тарифы",
        "Минимальные знания для проджуктивного роста во время менторства",
        "Я работаю и хочу апнуть зарплату или поменять компанию",
        placeholder="Выберите один из пунктов",
        sizes=(3, 1, 1)
    )
    )

@user_private_router.message(F.text == "Как проходит менторство?")
async def mentor_answer(message: types.Message):
    await message.answer("")

@user_private_router.message(F.text == "Хочу записаться к вам на мок-бес")
async def recording_mock_bes(message: types.Message):
    await message.answer("выберите один из пунктов", reply_markup=reply.get_keyboard(
        "Анонимно",
        "Для ютуба",
        placeholder="Выберите один из пунктов",
        sizes=(1, 1)
    )
    )


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

