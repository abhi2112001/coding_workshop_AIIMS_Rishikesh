import telebot
from libgen_api import LibgenSearch

API_KEY = "5693826777:AAFzUhCVbeREiq4zSj5L-dhh3h5Eps5q70k"
global msg
msg = ""

bot = telebot.TeleBot(API_KEY)
# SEARCH TOOL

start_message = "This is a book finding bot. Simply select whether you want to find the book by the Title or by Author's name. Kindly make sure that you type correct names. We do not promote any kind of piracy and strictly recommend you to purchase books. \n \n How do you want to search book - \n 1. /title_name \n 2. /author_name"


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id,start_message)

@bot.message_handler(commands=['title_name'])
def EnterTitleName(message):
    bot.send_message(message.chat.id,"Enter the name of your desired book")

    @bot.message_handler(func=lambda message: True)
    def getting_name(message):
        print("User typed: " + message.text)
        s = LibgenSearch()
        results = s.search_title(message.text)
        sending_book = ""

        for result in results:
            sending_book += "Title: " + result["Title"]
            sending_book += "\n"
            sending_book += "Author: " + result["Author"]
            sending_book += "\n"
            sending_book += "Year" + result["Year"]
            sending_book += "\n"
            sending_book += "Link 1: " + result["Mirror_1"]
            sending_book += "\n"
            sending_book += "Link 1: " + result["Mirror_2"]
            sending_book += "\n"
            sending_book += "Link 1: " + result["Mirror_3"]
            sending_book += "\n\n"

            print(result["Mirror_1"])

            bot.send_message(message.chat.id,sending_book)
            sending_book = ""
        return message



bot.polling()
