import request
import pyttsx3

def get_weather(city: str): -> str:
    base_url = f"https://wttr.in{city}?format=%C+%t"
    response = request.get(base_url)
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Не удалось получить данные о погоде. Пожалуйста, попробуйте позже."

def speak(text: str) -> None:
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAdnWait()