from aiogram.types import KeyboardButton,ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

logging.basicConfig(level=logging.INFO)
bot = Bot('6648810654:AAGV9mdU-EvMpg0vrz-2PtE0hfDgikiAl3A')
bots = Dispatcher(bot)
c1 = KeyboardButton("Lokatsiya",request_location=True)
cc = ReplyKeyboardMarkup(resize_keyboard=True).add(c1)
d1 = KeyboardButton("Lokatsiya",request_location=True)
dd = ReplyKeyboardMarkup(resize_keyboard=True).add(d1)

b1 = InlineKeyboardButton("Buyurtma qiling",callback_data="b1")
b2 = InlineKeyboardButton("Ortga qaytish",callback_data="b2")
byt = InlineKeyboardMarkup().add(b1,b2)
b1r = InlineKeyboardButton("Сделать заказ",callback_data="b1r")
b2r = InlineKeyboardButton("назад",callback_data="b2r")
bytr = InlineKeyboardMarkup().add(b1r,b2r )

byq = KeyboardButton("Geo-joylashuvni ko'rsating",request_location=True)
byq2 = KeyboardButton("orqaga")
byqq = ReplyKeyboardMarkup(resize_keyboard=True).add(byq).add(byq2)

byn = KeyboardButton("Telefon nomeringizni jonating",request_contact=True)
byn2 = KeyboardButton("orqaga")
bynq = ReplyKeyboardMarkup(resize_keyboard=True).add(byn).add(byn2)

bynr = KeyboardButton("Отправьте свой номер телефона",request_contact=True)
byn2r = KeyboardButton("назад")
bynqr = ReplyKeyboardMarkup(resize_keyboard=True).add(bynr).add(byn2r)


a1 = InlineKeyboardButton("TWISTER KEBAB ORIGINAL",callback_data='a1')
a2 = InlineKeyboardButton("burger",callback_data='a2')
a3 = InlineKeyboardButton("marojni",callback_data='a3')
ovaqat = InlineKeyboardMarkup().add(a1,a2,a3)


a1r = InlineKeyboardButton("TWISTER KEBAB ORIGINAL",callback_data='a1r')
a2r = InlineKeyboardButton("chiz burger",callback_data='a2r')
a3r = InlineKeyboardButton("ICE CREAM CONE",callback_data='a3r')
ovaqatr = InlineKeyboardMarkup().add(a1r,a2r,a3r)


cty = InlineKeyboardButton("Toshkent",callback_data="a")
cty1 = InlineKeyboardButton("Samarqand",callback_data="a")
cty2 = InlineKeyboardButton("Jizzah",callback_data="a")
cty3 = InlineKeyboardButton("Andijon",callback_data="a")
ctyy = InlineKeyboardMarkup().add(cty).add(cty1).add(cty2).add(cty3)
ctyr = InlineKeyboardButton("Ташкент",callback_data="b")
cty1r = InlineKeyboardButton("Самарканд",callback_data="b")
cty2r = InlineKeyboardButton("Джизак",callback_data="b")
cty3r = InlineKeyboardButton("Андижан",callback_data="b")
ctyyr = InlineKeyboardMarkup().add(ctyr).add(cty1r).add(cty2r).add(cty3r)



qwe = InlineKeyboardButton("Muloqot tili",callback_data='qwe')
qwe1 = InlineKeyboardButton("Telefon",callback_data='qwe1')
qwe2 = InlineKeyboardButton("shahar",callback_data='qwe2')
qww = InlineKeyboardMarkup().add(qwe,qwe1,qwe2)

qwer = InlineKeyboardButton("язык общения",callback_data='qwer')
qwe1r = InlineKeyboardButton("телефон",callback_data='qwe1r')
qwe2r = InlineKeyboardButton("город",callback_data='qwe2r')
qwwr = InlineKeyboardMarkup().add(qwer,qwe1r,qwe2r)


uzb = InlineKeyboardButton("Uzbek tili",callback_data='uzb')
rus = InlineKeyboardButton("Rus tili",callback_data='rus')


tilre = KeyboardButton("Tilni o'zgartirish")
tilre1 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(tilre)

tilre3 = KeyboardButton("Изменить язык")
tilre2 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(tilre3)


tillar = InlineKeyboardMarkup().add(uzb,rus)
USD = KeyboardButton("Buyurtma qilish")
RUB = KeyboardButton("Buyurmalarim")
EUR = KeyboardButton("Buyurmalarim")
SOZLAMALAR = KeyboardButton("Sozlamalar")

valyuta = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(USD,RUB).add(EUR,SOZLAMALAR)


США = KeyboardButton("заказать")
руб = KeyboardButton("мои заказы")
евро = KeyboardButton("комментарий")
настройки = KeyboardButton("настройки")

valyuta1 = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(США,руб).add(евро,настройки)


@bots.message_handler(commands=["start"])
async def til(message: types.Message):
    await message.reply(f"Tilni tanlang {message.from_user.last_name or message.from_user.first_name}",reply_markup=tillar)
    
@bots.callback_query_handler(lambda a:a.data)
async def inline(callback_query: types.CallbackQuery): 
    btn= callback_query.data
    if btn == "uzb":
        await bot.send_message(callback_query.from_user.id,text="siz Oz'bek tilini tanladingiz",reply_markup=valyuta)
    if btn == "rus":
        await bot.send_message(callback_query.from_user.id,text="вы выбрали русский язык",reply_markup=valyuta1)
    if btn == "a1":
        await bot.send_photo(callback_query.from_user.id,"https://kfc.com.uz/admin/files/5349.jpg",f"TWISTER KEBAB ORIGINAL\n2500 som",reply_markup=byt)
        
    if btn == "a2":
        await bot.send_photo(callback_query.from_user.id,"https://irecommend.ru/sites/default/files/product-images/1229813/bBQtzMMV60O71J6BLhnYng.jpeg",f"BIG SANDERS BURGER ORIGINAL\n6000 som",reply_markup=byt)
    if btn == "a3":
        await bot.send_photo(callback_query.from_user.id,"https://i.pinimg.com/originals/56/8e/a9/568ea91dcf8ea50d7cfed033caa54711.jpg",f"Ice cream 0cone\n4000 som",reply_markup=byt)
        
        
        
    if btn == "a1r":
        await bot.send_photo(callback_query.from_user.id,"https://kfc.com.uz/admin/files/5349.jpg",f"TWISTER KEBAB ORIGINAL\n2500 som",reply_markup=bytr)
    if btn == "a2r":
        await bot.send_photo(callback_query.from_user.id,"https://irecommend.ru/sites/default/files/product-images/1229813/bBQtzMMV60O71J6BLhnYng.jpeg",f"BIG SANDERS BURGER ORIGINAL\n6000 som",reply_markup=bytr)
    if btn == "a3r":
        await bot.send_photo(callback_query.from_user.id,"https://i.pinimg.com/originals/56/8e/a9/568ea91dcf8ea50d7cfed033caa54711.jpg",f"Ice cream 0cone\n4000 som",reply_markup=bytr)
        
        
    if btn == "b1":
        await bot.send_message(callback_query.from_user.id,f"30 daqiqada yetkaziladi",reply_markup=valyuta)
    if btn == "b2":
        
        await bot.send_message(callback_query.from_user.id,"Buyurtmani bekor qildingiz",reply_markup=valyuta)
    if btn == "b1r":
        await bot.send_message(callback_query.from_user.id,f"Доставили за 30 минут",reply_markup=valyuta1)
    if btn == "b2r":
        await bot.send_message(callback_query.from_user.id,f"Вы отменили заказ",reply_markup= valyuta1)
   
    if btn == 'qwe':
        await bot.send_message(callback_query.from_user.id,f"Tilni tanlang {callback_query.from_user.last_name or callback_query.from_user.first_name}",reply_markup=tillar)
    if btn == 'qwe1':
        await bot.send_message(callback_query.from_user.id,f"Muloqot tili: 🇺🇿 O'zbekcha\nTelefon: +998971739989\nShahar: Toshkent\nTelefon nomeringizni jonating",reply_markup=bynq)
    if btn == 'qwe2':
        await bot.send_message(callback_query.from_user.id,f"Muloqot tili: 🇺🇿 O'zbekcha\nTelefon: +998971739989\nShahar: Toshkent\nQuydagilardan birini tanlang",reply_markup=ctyy)
    if btn == "a":
        await bot.send_message(callback_query.from_user.id,f"shahar ozgartirildi",reply_markup=valyuta)
    if btn == "b":
        await bot.send_message(callback_query.from_user.id,f"город был изменен",reply_markup=valyuta1)
    if btn == 'qwer':
        await bot.send_message(callback_query.from_user.id,f"Выберите язык {callback_query.from_user.last_name or callback_query.from_user.first_name}",reply_markup=tillar)
    if btn == 'qwe1r':
        await bot.send_message(callback_query.from_user.id,f"Язык общения: 🇺🇿 Узбекский\nТелефон: +998971739989\nГород: Ташкент\nОтправьте свой номер телефона",reply_markup=bynqr)
    if btn == 'qwe2r':
        await bot.send_message(callback_query.from_user.id,f"Язык общения: 🇺🇿 Узбекский\nТелефон: +998971739989\nГород: Ташкент\nВыберите один из следующих",reply_markup=ctyyr)
        
    
        
        
        
@bots.message_handler()
async def til(message: types.Message):
    if message.text == 'Buyurtma qilish':
        await message.reply("Buyurtma qiling",reply_markup=ovaqat)
    if message.text == 'заказать':
            await message.reply("заказать",reply_markup=ovaqatr)
    if message.text == "orqaga":
            await message.reply("Quyidagilardan birini tanlang",reply_markup=valyuta)
        
    if message.text == "Sozlamalar":
        await message.reply(f"Muloqot tili: 🇺🇿 O'zbekcha\nTelefon: +998971739989\nShahar: Toshkent\nQuyidagilardan birini tanlangh",reply_markup=qww)
    if message.text == "Tilni o'zgartirish":
        await message.reply("Tilni o'zgartiring",reply_markup=tillar)
    if message.text == "настройки":
        await message.reply("Язык общения: 🇺🇿 Узбекский Телефон: +998971739989\nГород: Ташкент\nВыберите один из следующих",reply_markup=qwwr)
    if message.text == "Изменить язык":
        await message.reply("Изменить язык",reply_markup=tillar)
    if message.text == "Buyurtma qiling":
        await message.reply("buyurtma berdingiz",reply_markup=c1)
    if message.text == "Ortga qaytish":
        await message.reply("buyurtma bekor qildingiz",reply_markup=valyuta)
    if message.text == "назад":
        await message.reply("Вы отменили заказ",reply_markup=valyuta1)
            

if __name__ == '__main__':
  executor.start_polling(bots)



