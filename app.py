import asyncio
import os

from aiogram import (
    Bot,
    Dispatcher,
)

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from handlers.user_private import user_private_router

ALOOWED_OBDATES = [
    "message",
    "edited_message"
]

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_routers(user_private_router)


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALOOWED_OBDATES)


asyncio.run(main())
