import requests
import random
from bs4 import BeautifulSoup as b
import telebot

bot = telebot.TeleBot('5635813542:AAEVrQy3_OGnUME1MSzrCX2Et4zjtQFvNQk')

URL = 'https://bbf.ru/quotes/?character=184098' 

def parser(url):
    r = requests.get(URL)
    soup = b(r.text,'html.parser')
    citats = soup.find_all('div',class_='sentence__body')
    return [c.text for c in citats]

list_of_citats = parser(URL)
random.shuffle(list_of_citats)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет слага, я Тайлер Дерден на каждый день, и если ты хочешь получить от меня мои словечки напиши "цитата"')

@bot.message_handler(content_types=['text'])
def go(message):
    if message.text.lower() in 'цитата':
        bot.send_message(message.chat.id,list_of_citats[0])
        del list_of_citats[0]
    else:
        bot.send_message(message.chat.id,'Иди нахуй, напиши цитата долбоеб')

bot.polling(none_stop=True)
