import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Text, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import FSInputFile
from aiogram import F

token = '6652328511:AAFqdxLmmkP49gEMXO0HtXy_nRYdLngMcuc'


router = Router()


kb = [
    types.KeyboardButton(text='кнопка 1'),
    types.KeyboardButton(text='кнопка 2'),
]


@router.message(Text('Привет'))
async def send_image_file(message: types.Message):
    url = f'data/kek.png'
    task_image = FSInputFile(url)
    await message.answer.photo(
        photo=task_image,
        caption='Привет'
    )

@router.message(Command('/start'))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder
    for button in kb:
        builder.add(button)
    builder.adjust(2)
    await message.answer(text='abcdefgh',
                         reply_markup=builder.as_markup(resize_keyboard=True))



@router.message(Text('кнопка 1'))
async def hello(message: types.Message):
    await message.answer(text='ты выбрал кнопку 1')




@router.message(Text('Привет54321'))
async def send_file(message: types.Message):
    url = 'main.py'
    file = FSInputFile(url)
    await message.answer.document(
        document=file,
        caption='не обязательно подпись к файлу'
    )


@router.message(F.photo)
async def save_photo(message: types.Message, bot: Bot):
    await bot.download(message.photo[-1])
    destination = f'data/{message.photo[-1].file_id}.jpg'






async def main():
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(token, parse_mode='HTML')
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

    if __name__ == 'main':
        asyncio.run(main())