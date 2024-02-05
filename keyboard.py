from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

async def kb_subscride():
    builder_subscribe = InlineKeyboardBuilder()
    builder_subscribe.button(text="Подписаться",url = "https://t.me/angelikaryazanova")
    builder_subscribe.button(text="Подписка оформлена", callback_data="checkSubscride")
    builder_subscribe.adjust(1,1)
    return builder_subscribe.as_markup()

async def kb_guide():
    builder_subscribe = InlineKeyboardBuilder()
    builder_subscribe.button(text="Получить гайд",url = "https://telegra.ph/Kak-kosmetologu-ezhemesyachno-zarabatyvat-200000---500000-02-04")
    return builder_subscribe.as_markup()