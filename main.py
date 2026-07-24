import speech_recognition as sr
import pyttsx3
import config
import commands

# Инициализация синтеза речи
engine = pyttsx3.init()
engine.setProperty('volume', config.VOICE_VOLUME)
engine.setProperty('rate', config.VOICE_RATE)

# Инициализация распознавания речи
recognizer = sr.Recognizer()


def speak(text):
    """Произносит текст голосом"""
    print(f"🤖 {config.ASSISTANT_NAME}: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """Слушает и распознает речь"""
    try:
        with sr.Microphone() as source:
            print("🎤 Слушаю...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=config.TIMEOUT)
            
        print("⏳ Обработка речи...")
        text = recognizer.recognize_google(audio, language=config.LANGUAGE)
        print(f"👤 Вы сказали: {text}")
        return text
        
    except sr.UnknownValueError:
        speak("Извините, я не понял что вы сказали. Повторите пожалуйста.")
        return None
    except sr.RequestError:
        speak("Ошибка подключения к сервису распознавания речи.")
        return None
    except Exception as e:
        speak(f"Ошибка: {e}")
        return None


def main():
    """Главная функция"""
    print("=" * 50)
    print(f"  🤖 {config.ASSISTANT_NAME} V1.0")
    print("=" * 50)
    print("Скажите 'помощь' для справки по командам")
    print("Скажите 'выход' или 'пока' для завершения")
    print("=" * 50)
    
    speak(config.GREETING)
    
    while True:
        try:
            # Слушаем команду
            user_input = listen()
            
            if user_input is None:
                continue
            
            # Проверка на выход
            if "выход" in user_input.lower() or "пока" in user_input.lower() or "до свидания" in user_input.lower():
                speak("До свидания! Был рад помочь.")
                break
            
            # Обработка команды
            response = commands.process_command(user_input)
            speak(response)
            
        except KeyboardInterrupt:
            print("\n\nПрограмма завершена.")
            speak("До свидания!")
            break
        except Exception as e:
            print(f"Ошибка: {e}")
            speak(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()