import telebot
import os 

api = "7923180621:AAFRm1-fmfRmcYX3H5gng1l3rdhHHNePqMg"

bot = telebot.TeleBot(api)

def checkWebUsesInfo(message_chat, flags, value):
    if flags != "" and value != "":
        value =  os.system(f"python blackbird.py -{flags} {value}")
        bot.send_message(message_chat, value)
    else:
        bot.send_message(message_chat, "не заполнены поля")
        
@bot.message_handler(content_types=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Здравствуйте этот бот предстовляет собой инструмент по нахождению совподений по нику в интернете")

@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        # if message.text.strip() == "":
        #     bot.send_message(message.chat.id, "Ведите флаг поиска из ниже преведенных usage: blackbird [-h] [-u [USERNAME ...]] [-uf USERNAME_FILE] [--permute] [--permuteall] [-e [EMAIL ...]] [-ef EMAIL_FILE] [--csv | --no-csv] [--pdf | --no-pdf] [-v | --verbose | --no-verbose]m[-ai | --ai | --no-ai] [--filter FILTER] [--no-nsfw] [--dump] [--proxy PROXY] [--timeout TIMEOUT], [--max-concurrent-requests MAX_CONCURRENT_REQUESTS] [--no-update] [--about]")
        
        bot.send_message(message.chat.id, "Ведите флаг поиска")
        flag = message.text.strip()
        if flag != "":
            bot.send_message(message.chat.id, "Ведите имя пользователя")
            nameUser = message.text.strip()

        if flag != "" and nameUser != "":
            checkWebUsesInfo(message.chat.id, flag, nameUser)

    except Exception  as e:
        print(f"Error: {e}")

bot.polling(none_stop=True)