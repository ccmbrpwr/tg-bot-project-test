import telebot
from config import Keys, TOKEN
from extensions import APIException, Converter



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def help(message):
    bot.reply_to(message, "Чтобы начать работу введите команду по принципу: \n<Название валюты><В какую валюту перевести>\
<Кол-во переводимой валюты>\
\nУвидеть список всех доступных валют: /values")

@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты:'
    for key in Keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text'])
def convert(message):
    values = message.text.split(' ')

    if len(values) != 3:
        raise APIException('Недостаток или Переполнение параметров.')

    quote, base, amount = values
    final_base = Converter.get_price(quote, base, amount)
    text = f'Цена {amount} {quote} в {base} - {final_base}'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop = True)
