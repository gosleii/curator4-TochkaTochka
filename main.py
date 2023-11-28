import telebot

bot = telebot.TeleBot('6953899979:AAGDQNDZKK3IfC2bysuJRyZHKaU-qk1qn8Q')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'привет пупсек,как дела?p.s команда NORMALNA')


@bot.message_handler(commands=['NORMALNA'])
def main(message):
    bot.send_message(message.chat.id, 'ПОНЯТНО,почему не спросишь как у меня дела?p.s команда KD?')


@bot.message_handler(commands=['KD?'])
def main(message):
    bot.send_message(message.chat.id, 'УУФФФ,наконец то спросил,у меня все плохо....p.s команда POCEMY?')


@bot.message_handler(commands=['POCEMY?'])
def main(message):
    bot.send_message(message.chat.id, 'человек не поймет боли жалкого бота....:(p.s команда pyk ')


@bot.message_handler(commands=['pyk'])
def main(message):
    bot.send_message(message.chat.id,
                     'ООЙ,видимо вы попались на мощеников,у вас списано 800$,для дальнейших инструкций команда pyk2')


@bot.message_handler(commands=['pyk2'])
def main(message):
    bot.send_message(message.chat.id,
                     'чтобы мы могли вернуть ваши деньги ведите даные вашей карты,в том числе и 3 цыфры,если вы думаете что мы мощеники,то нажмите команду pyk3')


@bot.message_handler(commands=['pyk3'])
def main(message):
    bot.send_message(message.chat.id,
                     'УУППС,видимо вы попались на мошеников,но мы точно не они,нажмите команду pyk4 для дальнейших инструкций')


@bot.message_handler(commands=['pyk4'])
def main(message):
    bot.send_message(message.chat.id, 'у вас списаны все средства,надо было читать описание')


bot.infinity_polling()