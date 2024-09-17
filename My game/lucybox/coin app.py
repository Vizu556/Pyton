from aiogram import Bot, executor, Dispatcher, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7205718661:AAG7VC2H52v7u46D4FonIXvFuqeY2S2Vmy4')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Play "FruitCoin"', web_app=WebAppInfo(url='https://f661-80-246-94-239.ngrok-free.app')))
    markup.add(types.InlineKeyboardButton('Join Community', url='https://t.me/FruitC0in'))
    await message.answer( 'Привет! Добро пожаловать в Fruit Coin! Отныне ты владелец фруктового сада! Какого именно? Решать тебе. Тапай по экрану и улучшай свой сад!', reply_markup=markup)


executor.start_polling(dp)