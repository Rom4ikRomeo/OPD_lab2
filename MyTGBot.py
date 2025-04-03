import asyncio
import logging
import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Токен бота
TOKEN = "МойТокен"

# Создаем объекты бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Задаём рандомное число от 1 до 100
secret_number = random.randint(1, 100)

@dp.message(Command("start")) # когда пишем в боте /start
async def send_welcome(message: Message):
    await message.answer("Привет! Я загадал число от 1 до 100. Попробуй угадать!") # отправление приветственного сообщения

# Обработчик сообщений
@dp.message()
async def guess_number(message: Message):
    global secret_number # Позволяет менять переменнуб внутри функции
    if message.text.isdigit(): # состоит ли сообщение только из цифр
        guess = int(message.text) # превращает наше сообщение в int
        # Проверяем, угадал ли пользователь число
        if guess < secret_number:
            await message.answer("Загаданное число больше!") # даём пользователю подсказку
        elif guess > secret_number:
            await message.answer("Загаданное число меньше!")
        else:
            await message.answer("Поздравляю! Ты угадал число! Теперь я загадаю новое. Угадывай.")
            secret_number = random.randint(1, 100)  # Загадываем новое число
    else:
        await message.answer("Пожалуйста, введи число от 1 до 100.") # если сообщение состоит не из цифр

async def main():
    await dp.start_polling(bot) # запуск бота

if __name__ == "__main__":
    asyncio.run(main()) # запуск асинхронного цикла работы бота