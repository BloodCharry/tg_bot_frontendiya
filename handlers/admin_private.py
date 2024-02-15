from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from filters.chat_types import ChatTypeFilter, IsAdmin
from keyboards import reply
from keyboards.reply import get_keyboard

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())

ADMIN_KB = get_keyboard(
    "Управление пользователями",
    "Настройка сообщений",
    "Настройки бота",
    "Аналитическая информация",
    placeholder="Выберите действие",
    sizes=(2, 1, 1),
)


@admin_router.message(Command("admin"))
async def select_option(message: types.Message):
    await message.answer("Что хотите сделать?", reply_markup=ADMIN_KB)


class AdminFSM(StatesGroup):
    user_management = State()
    setup_messages = State()
    setup_bot = State()
    analytics_info = State()


@admin_router.message(F.text == "Управление пользователями")
async def user_settings(message: types.Message, state: FSMContext):
    await message.answer("выберите один из пунктов", reply_markup=reply.get_keyboard(
        "Список пользователей",
        "Удалить пользователя",
        "Изменить данные пользователя",
        "Блокировать пользователя",
        "Разблокировать пользователя",
        placeholder="Выберите один из пунктов",
        sizes=(2, 2, 1)
    ))


@admin_router.message(F.text == "Настройка сообщений")
async def message_settings(message: types.Message, state: FSMContext):
    await message.answer("выберите один из пунктов", reply_markup=reply.get_keyboard(
        "Просмотреть список сообщений",
        "Удалить сообщение",
        "отклонить сообщение",
        placeholder="Выберите один из пунктов",
        sizes=(1, 1, 1)
    )
                         )


@admin_router.message(F.text == "Настройки бота")
async def bot_setup(message: types.Message, state: FSMContext):
    await message.answer("Выберите категорию для настройки",
                         reply_markup=reply.get_keyboard(
                             "Название бота",
                             "Описание бота",
                             "Аватар",
                             placeholder="Выберите один из пунктов",
                             sizes=(1, 1, 1)
                         )
                         )


@admin_router.message(F.text == "Аналитическая информация")
async def analytics(message: types.Message, state: FSMContext):
    await message.answer("Выберите категорию:",
                         reply_markup=reply.get_keyboard(
                             "Статистика посещений",
                             "актвность пользователей",
                             placeholder="Выберите один из пунктов",
                             sizes=(1, 1)
                         )
                         )


@admin_router.message(Command("назад"))
@admin_router.message(F.text.casefold() == "назад")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:
    await message.answer(f"ок, вы вернулись к прошлому шагу")
