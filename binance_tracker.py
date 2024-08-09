
import time
from binance.client import Client
from telegram import Bot

# Установите ваш API ключ и секретный ключ Binance
binance_api_key = 'YOUR_BINANCE_API_KEY'
binance_api_secret = 'YOUR_BINANCE_SECRET_KEY'

# Установите ваш Telegram токен и User ID
telegram_token = 'YOUR_TELEGRAM_TOKEN'
telegram_chat_id = 'YOUR_TELEGRAM_USER_ID'

# Инициализация клиентов Binance и Telegram
client = Client(binance_api_key, binance_api_secret)
bot = Bot(token=telegram_token)

def get_price_change(symbol, interval='1m'):
    candles = client.get_klines(symbol=symbol, interval=interval)
    close_prices = [float(candle[4]) for candle in candles]
    
    if len(close_prices) >= 2:
        return ((close_prices[-1] - close_prices[-2]) / close_prices[-2]) * 100
    return 0

def track_price_changes():
    symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']  # добавьте сюда нужные пары
    threshold = 1  # Порог изменения цены в процентах для уведомления
    
    while True:
        for symbol in symbols:
            try:
                change = get_price_change(symbol)
                if abs(change) >= threshold:
                    message = f"🚀 {symbol} изменилась на {change:.2f}% за последнюю минуту!"
                    bot.send_message(chat_id=telegram_chat_id, text=message)
            except Exception as e:
                # Отправка ошибки в Telegram и продолжение работы
                error_message = f"Ошибка при обработке {symbol}: {e}"
                bot.send_message(chat_id=telegram_chat_id, text=error_message)
        time.sleep(60)  # Ожидание перед следующим циклом

if __name__ == "__main__":
    while True:
        try:
            track_price_changes()
        except Exception as e:
            # Отправка ошибки в Telegram и продолжение работы
            bot.send_message(chat_id=telegram_chat_id, text=f"Ошибка в основном цикле: {e}")
