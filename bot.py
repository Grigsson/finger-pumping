import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
import asyncio

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Укажите токен вашего бота
API_TOKEN = "" 

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: Message):
    logging.info("Получена команда /start")
    welcome_text = (
        "Привет! Добро пожаловать в FingerPumping💪! Для тебя открывается новый мир - мир онлайн пампинга!\n\n"
        "В этой увлекательной мини-игре ты сможешь сам контролировать путь своего качка, начиная от щуплого мальчика "
        "и заканчивая мышечным бумом!\n\n"
        "Тапай, прокачивайся, зарабатывай валюту и соревнуйся с друзьями.\n\n"
        "Следи за ростом своего героя и побеждай в этой захватывающей битве за мускулы!"
    )

    # Создание кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Играть сейчас 💪", url="https://grigsson.github.io/finger-pumping/")],
        [InlineKeyboardButton(text="Подписаться на канал", url="https://t.me/+iacqDsJk5QI3NTAy")],
        [InlineKeyboardButton(text="Как играть", url="https://t.me/ССЫЛКА_НА_ИНСТРУКЦИЮ")]
    ])

    # Отправка сообщения с кнопками
    await message.answer(welcome_text, reply_markup=keyboard)

# Основная функция
async def main():
    logging.info("Запуск бота...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Запуск кода
if __name__ == "__main__":
    asyncio.run(main())
