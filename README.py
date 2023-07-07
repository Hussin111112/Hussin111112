import telebot

# استبدال TOKEN بتوكن البوت الخاص بك
bot = telebot.TeleBot('6309071008:AAHQ3SjCnGa53gqW4VSPRkpm2iNXY0xMvXw')

@bot.message_handler(commands=['start'])
def start(message):
    # افتح الملف من ذاكرة الجهاز
    with open('/storage/emulated/0/Pictures/Messenger/received_1249150522518779.jpeg', 'rb') as file:
        # استخدم وظيفة send_document لإرسال الملف
        bot.send_document(message.chat.id, file)

# استمرار تنفيذ البوت
bot.polling()
