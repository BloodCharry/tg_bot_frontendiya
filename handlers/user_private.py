from aiogram import (
    types,
    Router,
)
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def on_startup(message: types.Message):
    await message.answer("Привет, я виртуальный помошник")


@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("Мой меню:\n\n1. Первый пункт\n2. Второй пункт\n3. Третий пункт")


@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("О нас:")


@user_private_router.message()
async def echo(message: types.Message):
    text = message.text

    if text in ["Привет", "привет", "hi", "Hi", "хай", "Хай", "hello", "Hello"]:
        await message.answer("И тебе привет!")
    elif text in ["Пока", "пока", "bye", "Bye", "goodbye", "Goodbye", "до свидания", "До свидания"]:
        await message.answer("И тебе пока!")
    else:
        await message.reply("Я пока что не умею отвечать на такие вопросы")
