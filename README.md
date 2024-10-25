# Easy to Start Service
## Что тебе нужно сделать чтобы начать:
1. Ставишь 3 python. Версия на которой все изначально написано - 3.12.2
2. Делаешь git clone git@github.com:Drozdetskiy/easy_to_start.git через консоль в папке где будешь работать
3. cd easy_to_start - переход в папку easy_to_start
4. Делаешь python3 -m venv venv - это создаст папку venv со средой в которую ты будешь ставить нужные тебе пакеты
5. source venv/bin/activate - это активирует среду для установки пакетов. Она называется виртуальным окружением
6. pip install -r requirements.txt - это поставит пакеты в активированную среду
7. cd src - переход в папку с основным кодом
8. python3 manage.py run-http - это запустит сервер
9. Теперь открываешь браузер и вводишь http://0.0.0.0:9001/v1/main/ по этому адресу произойдет обращение к 
твоему серверу и выполнит описанную логику. Обрати внимание на то, что будет напечатано в консоли

Посмотри на комментарии в коде. Я постарался описать то что делает код. Пока тебе не обязательно знать как именно это 
работает. Постарайся просто посмотреть на основные конструкции и поэксперментируй с файлом main.py

Для того чтобы выключить сервер нажми ctrl + C в консоли
Изменения в коде вступят в силу только после перезапуска сервера

## Успехов!