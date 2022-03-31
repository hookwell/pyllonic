import telebot

bot = telebot.TeleBot("5295887032:AAH-S_BHTMXqZK8wIUt1FigKNk8HsRpC2hg")
@bot.message_handler(commands=["help","start"])

def enviar(message):
  bot.reply_to(message, "привет, как дела ?")


@bot.message_handler(func=lambda mensaje:True)
def mensaje(mensaje):
  bot.reply_to(mensaje, mensaje.text)


bot.polling()