import asyncio
import os

from aiogram import (
    Bot,
    Dispatcher,
    types
)

from aiogram.filters import CommandStart

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

bot = Bot(token=os.get_env("TOKEN"))
dp = Dispatcher()


@dp.message(CommandStart())
async def on_startup(message: types.Message):
    await message.answer("Это была команда старт!")


@dp.message()
async def echo(message: types.Message):
    text = message.text

    if text in ["Привет", "привет", "hi", "Hi", "хай", "Хай", "hello", "Hello"]:
        await message.answer("И тебе привет!")
    elif text in ["Пока", "пока", "bye", "Bye", "goodbye", "Goodbye", "до свидания", "До свидания"]:
        await message.answer("И тебе пока!")
    else:
        await message.reply("Я пока что не умею отвечать на такие вопросы")


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
