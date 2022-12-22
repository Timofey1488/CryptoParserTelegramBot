## This is my own project and first experience with binance api
All process i written here..
### Functions, that I already written
#### 1)Function start - show tutorial about telegram bot, stop - stopped timer
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
#### 2) If you enter integer number - timer is started

```python
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
```
