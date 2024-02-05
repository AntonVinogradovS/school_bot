import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandStart
from handlers import user_router, admin_router
from createBot import bot
#from database import on_startup
dp = Dispatcher()

dp.include_router(user_router)
dp.include_router(admin_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    #await on_startup()
    await dp.start_polling(bot)
    

if __name__ == "__main__": 
    asyncio.run(main())

