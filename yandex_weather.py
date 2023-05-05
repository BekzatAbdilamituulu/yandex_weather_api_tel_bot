import telebot, requests, json

bot = telebot.TeleBot('5438643044:AAFozgFfB3oRxcu9_alCnZr9ygzcDNncFL0')
url = "https://api.weather.yandex.ru/v2/informers?lat=42.8670976&lon=74.6061824"
headers = { "X-Yandex-API-Key": "972c7126-c5a5-4f25-8f1a-8fec42406f66"}

@bot.message_handler(commands=['start'])
def get_watherr(message):
    bot.send_message(message.chat.id, text=f'Привееет, {message.from_user.username}!\n\nЯ могу показать вам погоду с:\n/get_weather')
@bot.message_handler(commands=['get_weather'])

def get_weather(message):
    r = requests.get(url=url, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        fact = data["fact"]
        now_dt = dict(data).get("now_dt")
        

        bot.send_message(message.chat.id, text=f'Сегодня {now_dt[:10]} {now_dt[11:17]} в Бишкеке максимальная температура: {fact["temp"]}°C\nСкорость ветра: {fact["wind_speed"]}м/с\nДавление: {fact["pressure_pa"]} в гектопаскалях\nВлажность воздуха: {fact["humidity"]} %')

    else:
        bot.send_message(message.chat.id, 'Проблемы с API')


bot.polling(non_stop=True, interval=0)

