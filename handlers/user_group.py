from string import punctuation

from aiogram import (
    F,
    types,
    Router
)

user_group_router = Router()

restricted_words = {
    'лох', 'пидр', 'сука', 'блять', 'еблан',
}


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(message.text.lower().split()):
        await message.answer(f"{message.from_user.first_name}, соблюдайте порядок в чате!")
        await message.delete()
        # await message.chat.ban(user_id=message.from_user.id)
    else:
        await message.reply(
            f"{message.from_user.first_name}, я пока не могу ответить на этот вопрос"
        )
