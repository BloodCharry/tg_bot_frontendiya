from aiogram import (
    types,
    Router,
    F
)
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def on_startup(message: types.Message):
    await message.answer("Привет, я виртуальный помошник, чем могу помочь?")


@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer("Мой меню:\n\n1. Первый пункт\n2. Второй пункт\n3. Третий пункт")


@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message):
    await message.answer("О нас:")


@user_private_router.message(F.text.lower().in_(
    [
        'привет', 'hi', 'хай', 'hello'
    ]
))
async def echo_hello(message: types.Message):
    await message.answer("И тебе привет!")


@user_private_router.message(F.text.lower().in_(
    [
        "пока", "bye", "goodbye", "до свидания", "прощай", "до свидания"
    ]
))
async def echo_by(message: types.Message):
    await message.answer("И тебе пока!")
