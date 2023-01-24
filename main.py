import logging
from aiogram import Bot, Dispatcher, types
import asyncio
from PyEasyQiwi import QiwiConnection
import time
import os
import sqlite3
from db import select,first_time,create_user,creat_link,chek_oplacheno
api_key = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjJ0dDUyaS0wMCIsInVzZXJfaWQiOiI3OTgxMDE3ODcwNiIsInNlY3JldCI6ImY0Mzc4MDBhZDdlM2E3ZGUwYTcxNmEwN2QyY2JlZGFlYzE3NzIwMmFhYTU5NjI1NGM3MjQwZWVjN2Y5MThiMjQifX0="
conn = QiwiConnection(api_key)

con = sqlite3.connect("vpn.db")
cur = con.cursor()

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5753664893:AAHW4PFyy3BByZyWcgw9M8iSv-fs8iGKC1g")
dp = Dispatcher(bot)




@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    if first_time(message.from_user.id):
        create_user(message.from_user.id)
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
        builder = types.ReplyKeyboardMarkup(resize_keyboard=True)
        builder.row(types.KeyboardButton(
            text="Тарифы",
            callback_data="tariffs")
        )
        builder.insert(types.KeyboardButton(
            text="Мой тариф\n",
            callback_data="mytarif")
        )
        builder.row(types.KeyboardButton(
            text="Поддержка\n",
            callback_data="support")
        )
        builder.insert(types.KeyboardButton(
            text="FAQ\n",
            callback_data="FAQ")
        )
        builder.insert(types.KeyboardButton(
            text="Инструкция\n",
            callback_data="instruction")
        )
        await message.answer("Вы в главном меню", reply_markup=builder)



@dp.callback_query_handler(text='try_yes')
async def cmd_start(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup(resize_keyboard=True)
    builder.row(types.InlineKeyboardMarkup(
        text="App Store",
        url='https://apps.apple.com/us/app/outline-app/id1356177741'
    ),types.InlineKeyboardButton(
        text="Play Market",
        url='https://play.google.com/store/apps/details?id=org.outline.android.client&hl=en&gl=US')
    )
    builder.add(types.KeyboardButton(
        text="Что дальше?",
        callback_data="what_next")
    )
    await callback.message.answer(text="Супер, мой ВПН работает внутри приложения 'Outline'\nВам нужно его скачать, вот ссылки :",reply_markup=builder)



@dp.callback_query_handler(text='what_next')
async def cmd_start(callback: types.CallbackQuery):
    builder = types.InlineKeyboardMarkup()
    builder.add(types.InlineKeyboardButton(
        text="Супер",
        callback_data="main_menu")
    )
    await callback.message.answer("Вот ваш ключ для подключения к ВПНу:\nсообщение с ключом.")
    await asyncio.sleep(3)
    await callback.message.answer("Инструкция для подключения.\n1)Скопируйте этот ключ\n2) Откройте приложение Outline\n3)Вам предложит вставить скопированный\nтекст из телеграма, соглашайтесь!\n4) Нажимайте 'Connect'\n5) Поздравляем, вы в интернете!",reply_markup=builder)

@dp.callback_query_handler(text='tariffs')
async def cmd_start(callback: types.CallbackQuery):
    builder = types.ReplyKeyboardMarkup(resize_keyboard=True)
    builder.row(types.InlineKeyboardButton(
        text="Месяц",
        callback_data="first")
    )
    builder.insert(types.InlineKeyboardButton(
        text="3 Месяца",
        callback_data="second")
    )
    builder.row(types.InlineKeyboardButton(
        text="Целый год",
        callback_data="third")
    )
    builder.add(types.KeyboardButton(
        text="Главное меню",
        callback_data="what_next")
    )
    await callback.message.answer("Выбирайте любой удобный вариант:",reply_markup=builder)
@dp.message_handler(text='Тарифы')
async def cmd_start(message: types.Message):
    builder = types.ReplyKeyboardMarkup(resize_keyboard=True)
    builder.row(types.InlineKeyboardButton(
        text="Месяц",
        callback_data="first")
    )
    builder.insert(types.InlineKeyboardButton(
        text="3 Месяца",
        callback_data="second")
    )
    builder.row(types.InlineKeyboardButton(
        text="Целый год",
        callback_data="third")
    )
    builder.add(types.KeyboardButton(
        text="Главное меню",
        callback_data="what_next")
    )
    await message.answer("Выбирайте любой удобный вариант:",reply_markup=builder)



@dp.callback_query_handler(text='main_menu')
async def cmd_start(callback: types.CallbackQuery):
    builder = types.ReplyKeyboardMarkup(resize_keyboard=True)
    builder.row(types.KeyboardButton(
        text="Тарифы",
        callback_data="tariffs")
    )
    builder.insert(types.KeyboardButton(
        text="Мой тариф",
        callback_data="mytarif")
    )
    builder.row(types.KeyboardButton(
        text="Поддержка",
        callback_data="support")
    )
    builder.insert(types.KeyboardButton(
        text="FAQ",
        callback_data="FAQ")
    )
    builder.insert(types.KeyboardButton(
        text="Инструкция\n",
        callback_data="instruction")
    )
    await callback.message.answer("Вы в главном меню", reply_markup=builder)

@dp.message_handler(text='Главное меню')
async def cmd_start(message: types.Message):
    builder = types.ReplyKeyboardMarkup(resize_keyboard=True)
    builder.row(types.KeyboardButton(
        text="Тарифы",
        callback_data="tariffs")
    )
    builder.insert(types.KeyboardButton(
        text="Мой тариф\n",
        callback_data="mytarif")
    )
    builder.row(types.KeyboardButton(
        text="Поддержка\n",
        callback_data="support")
    )
    builder.insert(types.KeyboardButton(
        text="FAQ\n",
        callback_data="FAQ")
    )
    builder.insert(types.KeyboardButton(
        text="Инструкция\n",
        callback_data="instruction")
    )
    await message.answer("Вы в главном меню", reply_markup=builder)
@dp.message_handler(text='FAQ')
async def cmd_start(message: types.Message):
    await message.answer("""Что такое VPN и зачем оно мне?

VPN это виртуальная частная сеть которая, используя цифровой туннель, «переносит» вас в ту страну, где находится сервер VPN. В нашем случае в Великобританию , Финляндию  или Германию . Нужно это бывает в случаях когда внутри вашей страны некоторые сайты не работают.


Получил ссылку. Дальше что?

Ссылка это и есть ваш персональный ключ, который подключает вас к нашему серверу VPN. Если вы сделали всё по инструкции то включение и выключение VPN будет происходить через приложение Outline нажатием одной кнопки подключить / отключить.


А что с безопасностью и легально ли использование VPN? 

Использовать VPN можно. Товарищ майор ничего вам не сделает. Если вы конечно не собираетесь заниматься противозаконными вещами, но для этого лучше изучайте методы шифрования и купите лучше собственный сервер где-нибудь далеко). Ваш трафик мы нигде не собираем и физически не можем анализировать, так как технология которую использует приложение Outline не позволяет это делать, а открытый код программы лишний раз это подтверждает.


Как проверить работает ли VPN?

Можете открыть сайт 2ip.ru и посмотреть в какой стране вас видит сайт. Должно быть написано Великобритания  или Финляндия  или Германия .


Нужно ли отключать VPN?

Обязательно! Дело в том, что многие наши сервисы наоборот не пускают никого из-за границы и работать они будут плохо или не будут вообще. Особенно страдают банки, госуслуги и российские сервисы.

Караул у меня ничего не грузит!

Для начала проверьте на сайте 2ip.ru в какой стране вас видит сайт. Если Россия, значит вы не включили VPN. Если не Россия, тогда проверьте скорость соединения. Для этого чуть ниже на той же странице можно запустить тестирование скорости соединения. Если она отличается от нулевой, значит проблема не в VPN, а в настройках телефона. Тест должен показать скорость VPN сервера от 20 до 100 Мбит.

Если у вас нормальная скорость, но всё равно ничего не работает - попробуйте удалить приложение Outline, перезагрузить телефон и установить заново с вашим ключом из раздела "Мой тариф".
Если и это не помогло - пишите в техподдержку мы поможем.
Обязательно напишите модель телефона и кто у вас провайдер / оператор связи.""")

@dp.message_handler(text='Поддержка')
async def cmd_start(message: types.Message):
    await message.answer("""Перед тем как задать вопрос, обязательно прочитайте подробную инструкцию и раздел FAQ.
Для ускорения решения технических вопросов, можете сразу прислать скриншот с открытым приложением Outline и сообщение от бота из раздела "Мой тариф".
Ваши вопросы и обращения направлять сюда @simple_vpn_support""")

@dp.message_handler(text="Месяц")
async def cmd_start(message: types.Message):
    pay_url, bill_id, response=conn.create_bill(value=1.00,description=str(int(message.from_user.id)),theme_code='Egor-ChYZVzq4Ixq')
    builder = types.InlineKeyboardMarkup()
    print(message.from_user.id,pay_url,str(bill_id.replace(':','A',1)),"WAITED")
    creat_link(message.from_user.id,pay_url,str(bill_id.replace(':','A',1)),"WAITED")
    builder.add(types.InlineKeyboardButton(
        text="Сылка на оплату ",
        url=pay_url
    )
    )
    builder.add(types.InlineKeyboardButton(
        text='Поодтвердить отправку',
        callback_data='chek_oplat'))
    await message.answer(reply_markup=builder)

@dp.callback_query_handler(text='chek_oplat')
async def cmd_start(callback: types.CallbackQuery):

    await callback.message.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())