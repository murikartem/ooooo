from aiogram import types
from aiogram.filters import Text
from loader import router


@router.message(Text(contains='Привет'))
async def hello(message: types.Message):
    await message.answer(text='hello')