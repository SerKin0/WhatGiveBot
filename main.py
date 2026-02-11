from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from source.settings import TOKEN_BOT
from source.logs.logger import logger

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher()


@dp.message(Command(commands="start"))
async def process_start_command(message: Message):
    await message.answer("Привет")
    logger.info(f"Выведено стартовое сообщение")


if __name__ == '__main__':
    dp.run_polling(bot)
