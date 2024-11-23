import telebot

bot=telebot.TeleBot("7395550212:AAHA0rafNLja8mYocx_FUbk_IUitsDqU-xk")

#برای دکمه شیشه ای
first_button=telebot.types.InlineKeyboardButton("playlist",url="https://t.me/amiralimusicsa")  #این برای فرستادن به کانال
second_button=telebot.types.InlineKeyboardButton("button 2",callback_data="HI")   #این برای فرستادن نوتیف
markup=telebot.types.InlineKeyboardMarkup(row_width=1)
markup.add(first_button,second_button)
#برای حواب پیام
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    bot.answer_callback_query(call.id,"you clicked <HI> button")


@bot.message_handler(commands=['start'])
def start_message(message):
   bot.send_message(message.chat.id," hello ",reply_markup=markup) 
   
#برای ساخت دکمه های کیبورد  
key_markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
key_markup.add("information","two","three")  

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,"how can i help you?",reply_markup=key_markup)  
    
#یرای ثبت اطلاعات
@bot.message_handler(func=lambda m:True)
def info(message):
    if message.text=="information":
        msg=bot.send_message(message.chat.id,"enter your name:")
        bot.register_next_step_handler(msg,name)
def name(message):
    global nm
    nm=message.text
    msg=bot.send_message(message.chat.id,"enter your age:")
    bot.register_next_step_handler(msg,age)
def age(message):
    global ag
    ag=message.text
    msg=bot.send_message(message.chat.id,"enter your tall:")
    bot.register_next_step_handler(msg,tall)
def tall(message):
    gh=message.text
    bot.send_message(message.chat.id,f"your name is {nm}\n your age is {ag}\n your tall is {gh}")     
                 



bot.infinity_polling()  #برای اجرا