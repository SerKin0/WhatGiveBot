from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from source.keyboards.reply import create_start_keyboard
from source.log.logger import logger

router_commands = Router()


@router_commands.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        """✨ Добро пожаловать в бота «Что подарить?»! ✨

Тот самый помощник, который навсегда решит проблему с подарками.

Создайте свой вишлист, добавьте в него ссылки на товары из любых магазинов и легко делитесь списком с друзьями и семьей.

Давайте создадим ваш первый список желаний! Просто напишите, что бы вы хотели получить в подарок?""",
        reply_markup=create_start_keyboard(),
    )
    logger.info("Стартовое сообщение")


@router_commands.message(Command("help"))
async def help_command(message: Message):
    await message.answer("""""")
