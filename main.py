from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from source.settings import TOKEN_BOT
from source.logs.logger import logger
from source.keyboards.reply import create_start_keyboard


bot = Bot(token="8369386871:AAFRMMoiWKBWdf48WdiVqFg4hGOvPIGRRNY")
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("""✨ Добро пожаловать в бота «Что подарить?»! ✨
    
Тот самый помощник, который навсегда решит проблему с подарками.

Создайте свой вишлист, добавьте в него ссылки на товары из любых магазинов и легко делитесь списком с друзьями и семьей.

Давайте создадим ваш первый список желаний! Просто напишите, что бы вы хотели получить в подарок?""",
    reply_markup=create_start_keyboard)
    logger.info(f"Start message")


@dp.message(Command("help"))
async def help_command(message: Message):
    await  message.answer("""""")


@dp.message(Command(commands="data"))
async def get_data_user(message: Message):
    print(message)

if __name__ == '__main__':
    dp.run_polling(bot)
