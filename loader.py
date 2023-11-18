from aiogram import Bot, Dispatcher, Router


token = '6652328511:AAFqdxLmmkP49gEMXO0HtXy_nRYdLngMcuc'
router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(token, parse_mode='HTML')