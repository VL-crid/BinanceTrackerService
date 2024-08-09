
# Binance Tracker Service

Этот проект представляет собой Python-скрипт для отслеживания изменений цен на криптовалюты на платформе Binance. Скрипт работает в фоновом режиме как служба (сервис) на Windows и отправляет уведомления в Telegram, если цена какой-либо монеты изменилась на заданный процент.

## Установка

### 1. Установите необходимые библиотеки

```bash
pip install python-binance python-telegram-bot
```

### 2. Настройка скрипта

Откройте файл `binance_tracker.py` и вставьте ваш API ключ и секретный ключ Binance, а также ваш токен Telegram и User ID.

### 3. Настройка службы на Windows с помощью NSSM

1. Скачайте и установите NSSM с [официального сайта](https://nssm.cc/download).
2. Откройте командную строку от имени администратора и выполните следующие команды:

```cmd
cd C:\nssm\win64\
nssm install BinanceTrackerService
```

3. В открывшемся окне:
    - Укажите путь к `python.exe` в поле `Application Path`.
    - Укажите путь к вашему скрипту `binance_tracker.py` в поле `Arguments`.
    - Укажите рабочую директорию, где находится ваш скрипт, в поле `Startup Directory`.

4. Нажмите "Install Service".

### 4. Управление службой

Для управления службой используйте следующие команды:

- **Запуск службы:**

  ```cmd
  nssm start BinanceTrackerService
  ```

- **Остановка службы:**

  ```cmd
  nssm stop BinanceTrackerService
  ```

- **Перезапуск службы:**

  ```cmd
  nssm restart BinanceTrackerService
  ```

- **Удаление службы:**

  ```cmd
  nssm remove BinanceTrackerService
  ```

## Альтернативный метод с использованием `sc`

1. Создайте `batch` файл, например, `start_tracker.bat`:

```bat
@echo off
cd C:\path\to\your\script\
python binance_tracker.py
```

2. Создайте службу с помощью команды:

```cmd
sc create BinanceTrackerService binPath= "C:\path\to\start_tracker.bat"
```

3. Управление службой:

```cmd
sc start BinanceTrackerService
sc stop BinanceTrackerService
sc delete BinanceTrackerService
```

## Лицензия

Этот проект лицензирован под MIT License.
