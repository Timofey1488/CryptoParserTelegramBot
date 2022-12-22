from api import apikey, secret, botAPI
from binance import Client
from aiogram import Bot, Dispatcher, executor
import asyncio


checkTimer = True
bot = Bot(token=botAPI)
dp = Dispatcher(bot)

def parse_from_Binance():
    client = Client(apikey, secret)
    tickers = client.get_all_tickers()
    lst = []
    for item in tickers:
        if item['symbol'] == 'BTCBUSD':
            lst.append(f"Bitcoin/BTC:{round(float(item['price']))}")
        if item['symbol'] == 'ETHBUSD':
            lst.append(f"Ethereum/ETH:{round(float(item['price']),2)}")
        if item['symbol'] == 'XRPBUSD':
            lst.append(f"Ripple/XRP:{round(float(item['price']),4)}")
    str_list_data = "\n".join(lst)
    return str_list_data


@dp.message_handler(commands=['start'])
async def start_message(message):
    await bot.send_message(message.chat.id, "Hi, enter the number of minutes for the timer")
@dp.message_handler(commands=['stop'])
async def stop_message(message):
    global checkTimer
    checkTimer = False
    await bot.send_message(message.chat.id, "Timer is stopped")

@dp.message_handler()
async def start_message(message):
    try:
        timer_minutes = int(message.text)*60
        if timer_minutes <= 0:
            raise ValueError()

    except(TypeError, ValueError):
        await bot.send_message(message.chat.id, text="Write valid integer")
        return
    await bot.send_message(message.chat.id, text=f"Timer is worked every {message.text} min, to stop timer text /stop")
    while checkTimer:
        await bot.send_message(message.chat.id, str(parse_from_Binance()))
        await asyncio.sleep(timer_minutes)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




