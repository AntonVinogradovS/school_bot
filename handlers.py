from aiogram import types, Router
from aiogram.types import FSInputFile
from aiogram.filters.command import Command, CommandStart
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import F
from keyboard import kb_subscride, kb_guide
from createBot import bot
from message import mes_one, get_gaude

user_router = Router()

@user_router.message(CommandStart())
async def start_cmd(message: types.Message):
    #print(message.from_user.id)
    photo = FSInputFile(r'photo1.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=mes_one, parse_mode="HTML", reply_markup=await kb_subscride())

@user_router.callback_query(F.data == 'checkSubscride')
async def check_sub(callback: types.CallbackQuery):
    user_channel_status = await bot.get_chat_member(chat_id='@angelikaryazanova', user_id=callback.from_user.id)

    if user_channel_status.status == 'left':
        await callback.answer(text='Чтобы продолжить получить гайд, необходимо подписаться на канал', show_alert= True)
    else:
        # вытащить ссылку из бд
        #print(callback.from_user.first_name)
        await callback.message.answer(text=await get_gaude(callback.from_user.first_name), parse_mode="HTML", reply_markup=await kb_guide())

admin_router = Router()