import asyncio

from aiogram import Bot, Dispatcher

from source.handlers import buttons, commands
from source.settings import TOKEN_BOT


async def main():
    bot = Bot(token=TOKEN_BOT)
    dp = Dispatcher()

    dp.include_routers(commands.router_commands, buttons.router_buttons)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
