## This is my own project and first experience with binance api

#### Functions, that I already written

```python
@dp.message_handler(commands=['start'])
async def start_message(message):
    await bot.send_message(message.chat.id, "Hi, enter the number of minutes for the timer")
@dp.message_handler(commands=['stop'])
async def stop_message(message):
    global checkTimer
    checkTimer = False
    await bot.send_message(message.chat.id, "Timer is stopped")
```
