from aiogram import F, Router
from aiogram.types import Message

from source.logs.logger import logger

router_buttons = Router()


@router_buttons.message(F.text == "Добавить подарок 🎁")
async def add_wish(message: Message):
    await message.answer("Функция добавления подарка находится в разработке!")
    logger.info("Добавление подарка")


@router_buttons.message(F.text == "Изменить 🧰")
async def edit_wish(message: Message):
    await message.answer("Функция изменения подарка находится в разработке!")
    logger.info("Изменение подарка")
