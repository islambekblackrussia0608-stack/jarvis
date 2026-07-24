import os
import subprocess
import webbrowser
import config

def open_application(app_name):
    """Открывает приложение по названию"""
    app_name = app_name.lower().strip()
    
    if app_name in config.APPLICATIONS:
        try:
            os.startfile(config.APPLICATIONS[app_name])
            return f"Открываю {app_name}"
        except Exception as e:
            return f"Ошибка при открытии {app_name}: {e}"
    else:
        return f"Приложение {app_name} не найдено. Доступные: {', '.join(config.APPLICATIONS.keys())}"


def open_browser(browser_name="chrome"):
    """Открывает браузер"""
    browser_name = browser_name.lower().strip()
    
    if browser_name in config.BROWSERS:
        try:
            os.startfile(config.BROWSERS[browser_name])
            return f"Открываю {browser_name}"
        except Exception as e:
            return f"Браузер {browser_name} не установлен или не найден"
    else:
        webbrowser.open("https://www.google.com")
        return "Открываю браузер по умолчанию"


def search_google(query):
    """Поиск в Google"""
    try:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return f"Ищу в Google: {query}"
    except Exception as e:
        return f"Ошибка при поиске: {e}"


def search_youtube(query):
    """Поиск видео на YouTube"""
    try:
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        return f"Ищу на YouTube: {query}"
    except Exception as e:
        return f"Ошибка при поиске видео: {e}"


def shutdown_pc():
    """Выключение ПК"""
    try:
        os.system("shutdown /s /t 30")
        return "ПК выключится через 30 секунд"
    except Exception as e:
        return f"Ошибка при выключении: {e}"


def restart_pc():
    """Перезагрузка ПК"""
    try:
        os.system("shutdown /r /t 30")
        return "ПК перезагрузится через 30 секунд"
    except Exception as e:
        return f"Ошибка при перезагрузке: {e}"


def cancel_shutdown():
    """Отмена выключения"""
    try:
        os.system("shutdown /a")
        return "Выключение отменено"
    except Exception as e:
        return f"Ошибка при отмене: {e}"


def get_help():
    """Справка по командам"""
    help_text = """
    Доступные команды:
    - "Открой браузер" - открыть браузер
    - "Открой Chrome" - открыть Chrome
    - "Открой Firefox" - открыть Firefox
    - "Открой [название приложения]" - открыть приложение
    - "Ищи [запрос]" - поиск в Google
    - "Найди видео [запрос]" - поиск на YouTube
    - "Выключи компьютер" - выключить ПК через 30 сек
    - "Перезагрузи компьютер" - перезагрузить ПК через 30 сек
    - "Отмени выключение" - отменить выключение
    - "Помощь" - показать эту справку
    """
    return help_text


def process_command(command):
    """Обработка команды"""
    command = command.lower().strip()
    
    # Открыть браузер
    if "открой браузер" in command or "открой хром" in command or "открой chrome" in command:
        return open_browser("chrome")
    elif "открой firefox" in command or "открой файрфокс" in command:
        return open_browser("firefox")
    elif "открой edge" in command or "открой эдж" in command:
        return open_browser("edge")
    
    # Открыть приложение
    elif "открой" in command:
        app = command.replace("открой", "").strip()
        return open_application(app)
    
    # Поиск
    elif "ищи" in command or "найди" in command:
        query = command.replace("ищи", "").replace("найди", "").strip()
        return search_google(query)
    
    elif "видео" in command or "youtube" in command or "ютуб" in command:
        query = command.replace("видео", "").replace("youtube", "").replace("ютуб", "").strip()
        return search_youtube(query)
    
    # Управление ПК
    elif "выключи компьютер" in command or "выключение" in command:
        return shutdown_pc()
    elif "перезагрузи" in command or "перезагрузка" in command:
        return restart_pc()
    elif "отмени выключение" in command or "отмени" in command:
        return cancel_shutdown()
    
    # Справка
    elif "помощь" in command or "что ты можешь" in command:
        return get_help()
    
    # Приветствие
    elif "привет" in command or "здравствуй" in command or "привет джарвис" in command:
        return "Здравствуйте! Готов вас слушать."
    
    else:
        return "Команда не распознана. Скажите 'помощь' для справки."