import logging
from aiogram import Bot, Dispatcher, types
import asyncio
import sqlite3
import time
import os
import sqlite3
from db import select,first_time

con = sqlite3.connect("vpn.db")
cur = con.cursor()

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5753664893:AAHW4PFyy3BByZyWcgw9M8iSv-fs8iGKC1g")
dp = Dispatcher(bot)




@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    if message.from_user.id in [3727766,1890767310,'1890767310','3727766']:
        print(first_time(message.from_user.id))
        builder = types.InlineKeyboardMarkup()
        builder.add(types.InlineKeyboardButton(
            text="Да!",
            callback_data="try_yes")
        )
        builder.add(types.InlineKeyboardButton(
            text='Нет-хочу сразу купить тариф.',
            callback_data='tariffs'))
        await message.answer(
            text="Здравствуйте!\nРады что Вы обратились ко мне. Вам доступен бесплатный тестовый доступ на 2 дня,\nхотите попробовать?",reply_markup=builder
        )
    else:
        await message.answer('Пошел нахуй тебя не приглашали ')


@dp.callback_query_handler(text='try_yes')
async def cmd_start(callback: types.CallbackQuery):
    if callback.from_user.id in [3727766, 1890767310, '1890767310', '3727766']:
        builder = types.InlineKeyboardMarkup()
        builder.add(types.InlineKeyboardButton(
            text="App Store",
            url='https://apps.apple.com/us/app/outline-app/id1356177741'
        )
        )
        builder.add(types.InlineKeyboardButton(
            text="Play Market",
            url='https://play.google.com/store/apps/details?id=org.outline.android.client&hl=en&gl=US')
        )
        builder.add(types.InlineKeyboardButton(
            text="Что дальше?",
            callback_data="what_next")
        )
        await callback.message.answer(text="Супер, мой ВПН работает внутри приложения 'Outline'\nВам нужно его скачать, вот ссылки :",reply_markup=builder)
    else:
        await callback.message.answer('Пошел нахуй тебя не приглашали ')



@dp.callback_query_handler(text='what_next')
async def cmd_start(callback: types.CallbackQuery):
    if callback.from_user.id in [3727766, 1890767310, '1890767310', '3727766']:
        builder = types.InlineKeyboardMarkup()
        builder.add(types.InlineKeyboardButton(
            text="Супер",
            callback_data="main_menu")
        )
        await callback.message.answer("Вот ваш ключ для подключения к ВПНу:\nсообщение с ключом.")
        await asyncio.sleep(3)
        await callback.message.answer("Инструкция для подключения.\n1)Скопируйте этот ключ\n2) Откройте приложение Outline\n3)Вам предложит вставить скопированный\nтекст из телеграма, соглашайтесь!\n4) Нажимайте 'Connect'\n5) Поздравляем, вы в интернете!",reply_markup=builder)
    else:
        await callback.message.answer('Пошел нахуй тебя не приглашали ')


@dp.callback_query_handler(text='tariffs')
async def cmd_start(callback: types.CallbackQuery):
    if callback.from_user.id in [3727766, 1890767310, '1890767310', '3727766']:
        builder = types.InlineKeyboardMarkup()
        builder.add(types.InlineKeyboardButton(
            text="месяц",
            callback_data="first")
        )
        builder.add(types.InlineKeyboardButton(
            text="3 месяца",
            callback_data="second")
        )
        builder.add(types.InlineKeyboardButton(
            text="иди нахуй",
            callback_data="third")
        )
        await callback.message.answer("1 месяц 1 TON\n3 месяца 2.5 TON\n1 год 9 TON",reply_markup=builder)
    else:
        await callback.message.answer('Пошел нахуй тебя не приглашали ')


@dp.callback_query_handler(text='main_menu')
async def cmd_start(callback: types.CallbackQuery):
    if callback.from_user.id in [3727766, 1890767310, '1890767310', '3727766']:
        builder = types.InlineKeyboardMarkup()
        builder.add(types.InlineKeyboardButton(
            text="Тарифы",
            callback_data="tariffs")
        )
        builder.add(types.InlineKeyboardButton(
            text="месяц",
            callback_data="Мой-тариф")
        )
        builder.add(types.InlineKeyboardButton(
            text="Поддержка",
            callback_data="support")
        )
        builder.add(types.InlineKeyboardButton(
            text="FAQ",
            callback_data="FAQ")
        )
        await callback.message.answer("Вы в главном меню",reply_markup=builder)
    else:
        await callback.message.answer('Пошел нахуй тебя не приглашали ')
@dp.callback_query_handler(text='main_menu')
async def cmd_start(callback: types.CallbackQuery):
    if callback.from_user.id in [3727766, 1890767310, '1890767310', '3727766']:
        builder = types.InlineKeyboardMarkup()
        builder.add(types.InlineKeyboardButton(
            text="Тарифы",
            callback_data="tariffs")
        )
        builder.add(types.InlineKeyboardButton(
            text="месяц",
            callback_data="Мой-тариф")
        )
        builder.add(types.InlineKeyboardButton(
            text="Поддержка",
            callback_data="support")
        )
        builder.add(types.InlineKeyboardButton(
            text="FAQ",
            callback_data="FAQ")
        )
        await callback.message.answer("Вы в главном меню")
    else:
        await callback.message.answer('Пошел нахуй тебя не приглашали ')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())