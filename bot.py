import telebot
from config import token
from logic import get_weather

bot = telebot.Telebot(token)

@bot.message_handler(command=["start"])
def bot_start(message):
    bot.reply_to(
        message,
        f"Привет, {message.from_user.first_name}!\n"
        "Я бот прогноза погоды.\n"
        "Напиши /weather <город>, чтобы узнать погоду, например:\n"
        "/weather Moscow",
    )

    @bot.message_handler(commands=["weather"])
    def bot_weather(message):
        parts = message.text.split(maxsplit=1)
        if len(parts) < 2:
            bot.reply_to(message, "Пожалуйста, укажите город после команды /weather.")
            return
        else:
            city = parts(1)
            weather_info = get_weather(city)
            bot.reply_to(message, weather_info)
            speak(weather_info)


if __name__ == "__main__":
    bot.infinity_polling()