# Конфигурация JARVIS

# Имя ассистента
ASSISTANT_NAME = "JARVIS"

# Язык распознавания речи
LANGUAGE = "ru-RU"

# Время ожидания для микрофона (секунды)
TIMEOUT = 10

# Громкость синтеза речи (0.0 - 1.0)
VOICE_VOLUME = 0.9

# Скорость речи
VOICE_RATE = 150

# Приложения на Windows
APPLICATIONS = {
    "блокнот": "notepad",
    "калькулятор": "calc",
    "проводник": "explorer",
    "paint": "mspaint",
    "word": "winword",
    "excel": "excel",
    "powerpoint": "powerpnt",
}

# Браузеры
BROWSERS = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
    "edge": "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
}

# Приветствие
GREETING = f"Здравствуйте! Я {ASSISTANT_NAME}. Чем я вам могу помочь?"