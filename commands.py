import os
import subprocess
import webbrowser
from pathlib import Path
import psutil
import time

# Пути к приложениям и играм
STEAM_PATH = r"C:\Program Files (x86)\Steam\steamapps\common"
PROGRAM_FILES = r"C:\Program Files"
PROGRAM_FILES_X86 = r"C:\Program Files (x86)"

# Словарь для быстрого поиска
APPS_SHORTCUTS = {
    # Браузеры
    "хром": "chrome.exe",
    "хромиум": "chrome.exe",
    "гугл": "chrome.exe",
    "файрфокс": "firefox.exe",
    "браузер": "chrome.exe",
    
    # Мессенджеры
    "дискорд": "Discord.exe",
    "телеграм": "Telegram.exe",
    "вайбер": "Viber.exe",
    "скайп": "skype.exe",
    
    # Приложения
    "блокнот": "notepad.exe",
    "калькулятор": "calc.exe",
    "файлы": "explorer.exe",
    "стим": "steam.exe",
    "vs": "devenv.exe",
    "код": "code.exe",
    "паинт": "mspaint.exe",
    "ворд": "winword.exe",
    "эксель": "excel.exe",
    "пауэрпоинт": "powerpnt.exe",
    
    # Видео и медиа
    "кино": "vlc.exe",
    "видео": "vlc.exe",
    "влс": "vlc.exe",
    "проигрыватель": "wmplayer.exe",
    "фотографии": "photoviewer.dll",
}

def find_exe_in_directory(directory, exe_name):
    """Найти exe файл в директории"""
    try:
        if os.path.exists(directory):
            for file in os.listdir(directory):
                if file.lower() == exe_name.lower():
                    return os.path.join(directory, file)
    except:
        pass
    return None

def find_application(app_name):
    """Найти приложение на компе"""
    app_name_lower = app_name.lower().strip()
    
    # Проверить в словаре ярлыков
    if app_name_lower in APPS_SHORTCUTS:
        exe_name = APPS_SHORTCUTS[app_name_lower]
    else:
        exe_name = app_name_lower + ".exe" if not app_name_lower.endswith(".exe") else app_name_lower
    
    # Поиск в Program Files
    for directory in [PROGRAM_FILES, PROGRAM_FILES_X86]:
        exe_path = find_exe_in_directory(directory, exe_name)
        if exe_path:
            return exe_path
    
    # Поиск в System32
    system32_path = find_exe_in_directory(r"C:\Windows\System32", exe_name)
    if system32_path:
        return system32_path
    
    # Поиск в переменной PATH
    result = subprocess.run(f"where {exe_name}", shell=True, capture_output=True, text=True)
    if result.stdout.strip():
        return result.stdout.strip().split('\n')[0]
    
    return None

def find_steam_game(game_name):
    """Найти игру в Steam"""
    game_name_lower = game_name.lower().strip()
    
    try:
        if os.path.exists(STEAM_PATH):
            for folder in os.listdir(STEAM_PATH):
                if game_name_lower in folder.lower():
                    game_path = os.path.join(STEAM_PATH, folder)
                    # Найти exe файл
                    for file in os.listdir(game_path):
                        if file.endswith('.exe'):
                            return os.path.join(game_path, file)
    except:
        pass
    return None

def open_application(app_name):
    """Открыть приложение"""
    app_name = app_name.lower().strip()
    
    # Попробовать найти Steam игру
    game_exe = find_steam_game(app_name)
    if game_exe:
        try:
            subprocess.Popen(game_exe)
            return f"Запускаю {app_name}..."
        except:
            return f"Ошибка при запуске {app_name}"
    
    # Попробовать найти приложение
    app_exe = find_application(app_name)
    if app_exe:
        try:
            subprocess.Popen(app_exe)
            return f"Открываю {app_name}..."
        except:
            return f"Ошибка при открытии {app_name}"
    
    # Попробовать открыть как веб-сайт
    if "." in app_name and " " not in app_name:
        try:
            if not app_name.startswith("http"):
                app_name = "http://" + app_name
            webbrowser.open(app_name)
            return f"Открываю {app_name}..."
        except:
            pass
    
    # Попробовать открыть локальный файл
    if os.path.exists(app_name):
        try:
            os.startfile(app_name)
            return f"Открываю {app_name}..."
        except:
            return f"Не могу открыть {app_name}"
    
    return f"Не найден: {app_name}"

def close_application(app_name):
    """Закрыть приложение"""
    app_name_lower = app_name.lower().strip()
    
    # Получить exe имя
    if app_name_lower in APPS_SHORTCUTS:
        exe_name = APPS_SHORTCUTS[app_name_lower]
    else:
        exe_name = app_name_lower + ".exe" if not app_name_lower.endswith(".exe") else app_name_lower
    
    exe_name = exe_name.lower()
    closed = False
    
    # Найти процесс и закрыть его
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if exe_name in proc.info['name'].lower():
                proc.kill()
                closed = True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    if closed:
        return f"Закрыл {app_name}"
    else:
        return f"Не найден процесс: {app_name}"

def execute_command(command):
    """Выполнить команду"""
    command = command.lower().strip()
    
    # Открыть приложение
    if "открой" in command or "запусти" in command or "запустить" in command or "старт" in command:
        app_name = command.replace("открой", "").replace("запусти", "").replace("запустить", "").replace("старт", "").strip()
        if app_name:
            return open_application(app_name)
    
    # Закрыть приложение
    elif "закрой" in command or "выключи" in command or "убей" in command or "закрыть" in command:
        app_name = command.replace("закрой", "").replace("выключи", "").replace("убей", "").replace("закрыть", "").strip()
        if app_name:
            return close_application(app_name)
    
    # Интернет
    elif "интернет" in command or "сеть" in command:
        webbrowser.open("https://www.google.com")
        return "Открываю интернет..."
    
    # Помощь
    elif "помощь" in command or "что ты можешь" in command:
        return "Я могу открыть и закрыть любое приложение. Скажите 'открой [название]' или 'закрой [название]'"
    
    # Привет
    elif "привет" in command or "здравствуй" in command:
        return "Здравствуйте! Готов помочь."
    
    return "Команда не распознана"

def process_command(command):
    """Для совместимости"""
    return execute_command(command)
