from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from app import dp
from keyboards.inline_button import choose


@dp.message_handler(CommandStart())
async def bot_hello(message: types.Message):
    await message.answer("Hi 👋\nI can give you info about trade-pair. Select the desired button. ",
                         parse_mode=types.ParseMode.HTML,
                         reply_markup=choose)


@dp.message_handler()
async def bot_random(message: types.Message):
    await message.answer("Write only to the point. /start\nor shut up 😡", parse_mode=types.ParseMode.HTML)
