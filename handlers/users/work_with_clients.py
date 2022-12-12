from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import CallbackQuery
from app import dp
from keyboards.inline_button import choose, cancel
from states import Trades
from utils.services import logic_trade
import os


@dp.callback_query_handler(text="trade-pair")
async def cancel_button(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        "❗️ Please send me any trade-pair like the example below.\n\n"
        "<b>Example:</b> BTCUSDT",
        parse_mode=types.ParseMode.HTML)
    await Trades.Q1.set()


@dp.callback_query_handler(text="cancel", state='*')
async def cancel_button(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("👋 Bye-bye or click /start")


@dp.message_handler(state=Trades.Q1)
async def check_title(message: types.Message, state: FSMContext):
    try:
        await message.answer("Please wait...Do billing 🤔")

        img_url = logic_trade(message.text)

        await dp.bot.send_photo(chat_id=message.chat.id, photo=img_url)

    except:
        await message.answer("❗️ Please send me any trade-pair like the example below.\n\n"
                             "<b>Example:</b> BTCUSDT", parse_mode=types.ParseMode.HTML)

    await state.finish()
    await message.answer("👋 Bye-bye or click /start")
