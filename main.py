import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, BotCommand, InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
router = Router()

SITE_URL = 'https://sonifun.github.io/BIOSonifun'
SNAKE_URL = SITE_URL + '/snake.html'

COMMANDS = [
    BotCommand(command='portfolio', description='Портфолио'),
    BotCommand(command='snake', description='Играть в змейку'),
    BotCommand(command='contact', description='Как связаться'),
    BotCommand(command='links', description='Ссылки на портфолио и соцсети')
]


@router.message(Command(commands=["start", "bio", "BIO"]))
async def welcome(message: Message):
    welcome_text = (
        "<b>Привет!</b>\n"
        "Используй команды:\n"
        "• /portfolio — перейти на моё портфолио\n"
        "• /snake — играть в змейку\n"
        "• /contact — контакты\n"
        "• /links — ссылки на соцсети и ресурсы\n"
    )
    await bot.send_message(message.chat.id, welcome_text)

@router.message(Command("portfolio"))
async def portfolio(message: Message):
    portfolio_text = (
        "<b>Портфолио Sonifun</b>\n"
        "Здесь собраны мои проекты и навыки:\n"
        "• Telegram-боты\n"
        "• Веб-приложения и сайты\n"
        "• Автоматизация и ИИ-промты\n\n"
        "Перейти на сайт для полного портфолио:"
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Открыть сайт', url=SITE_URL)],
        [InlineKeyboardButton(text='Играть в змейку', url=SNAKE_URL)],
    ])
    await bot.send_message(message.chat.id, portfolio_text, reply_markup=keyboard)

@router.message(Command("contact"))
async def contact(message: Message):
    contact_text = (
        "<b>Контакты</b>\n"
        "Telegram: <a href='https://t.me/SonifunM'>@SonifunM</a>\n"
        "Discord: sonifunmt\n"
        "Email: sonifunmt@gmail.com\n"
        "Телефон: +7 995 684 98 36\n\n"
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Сайт', url=SITE_URL)],
        [InlineKeyboardButton(text='GitHub', url='https://github.com/Sonifun')],
    ])
    await bot.send_message(message.chat.id, contact_text, reply_markup=keyboard)


@router.message(Command("snake"))
async def snake(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Играть в змейку', url=SNAKE_URL)]
    ])
    await bot.send_message(message.chat.id, 'Змейка доступна здесь:', reply_markup=keyboard)

@router.message(Command("links"))
async def links(message: Message):
    links_text = (
        "<b>Мои ресурсы и контакты</b>\n\n"
        "<b>Портфолио:</b> Полный сайт с проектами\n"
        "<b>Игра:</b> Мини-игра Змейка\n"
        "<b>Telegram:</b> Пиши мне напрямую\n"
        "<b>GitHub:</b> Код и репозитории\n\n"
        "Выбери ссылку ниже:"
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Портфолио', url=SITE_URL), InlineKeyboardButton(text='Змейка', url=SNAKE_URL)],
        [InlineKeyboardButton(text='Telegram', url='https://t.me/SonifunM'), InlineKeyboardButton(text='GitHub', url='https://github.com/Sonifun')],
    ])
    await bot.send_message(message.chat.id, links_text, reply_markup=keyboard)

dp.include_router(router)

async def main():
    await bot.set_my_commands(COMMANDS)
    print('Bot started. Бот успешно запущен!')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())