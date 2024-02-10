import asyncio
import os

from aiogram import (
    Bot,
    Dispatcher,
)
from aiogram.enums import ParseMode

from aiogram.types import BotCommandScopeAllPrivateChats

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from common.bot_cmds import bot_commands

ALOOWED_OBDATES = [
    "message",
    "edited_message"
]

bot = Bot(token=os.getenv("TOKEN"),  parse_mode=ParseMode.HTML)
dp = Dispatcher()

dp.include_routers(user_private_router, user_group_router)


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    # если потребуется изменить меню, сначала нужно удалить старые команды
    # await bot.delete_my_commands(scope=BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=bot_commands, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALOOWED_OBDATES)


asyncio.run(main())
