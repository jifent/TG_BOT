from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

router = Router()

def get_main_reply_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text = '/Algorithms')]
        ],
        resize_keyboard = True
    )
    return keyboard

def get_main_reply_algo():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text = '/Sorting'), KeyboardButton(text = '/Linear')],
            [KeyboardButton(text = '/Strings'), KeyboardButton(text = '/Trees')]
        ],
        resize_keyboard = True
    )
    return keyboard

def algo_sort():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='/Algorithms')],
            [KeyboardButton(text = '/Murge_sort'), KeyboardButton(text = '/Quick_sort')]
        ],
        resize_keyboard = True
    )
    return keyboard

def algo_line():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='/Algorithms')],
            [KeyboardButton(text = '/Bin_search')]
            ],
            resize_keyboard = True)
    return keyboard

def algo_str():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='/Algorithms')],
            [KeyboardButton(text = '/Window'), KeyboardButton(text = '/INF_Input')],
            [KeyboardButton(text = '/Default_Functions')]
        ],
        resize_keyboard = True
    )
    return keyboard

def algo_tree():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='/Algorithms')],
            [KeyboardButton(text = '/DFS'), KeyboardButton(text = '/BFS')],
            [KeyboardButton(text = '/Dejkstra'), KeyboardButton(text = '/DO')]
        ],
        resize_keyboard = True
    )
    return keyboard

@router.message(Command("start"))
@router.message(F.text.lower() == "старт")
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}. Мы команда вайбкодеров, которая хочет пройти на ICPC", parse_mode = "HTML", reply_markup = get_main_reply_keyboard())

@router.message(Command("Algorithms"))
@router.message(F.text.lower() == "Algorithms")
async def algo(message: Message):
    await message.answer(text = ";)", parse_mode = "HTML", reply_markup = get_main_reply_algo())

@router.message(Command("Sorting"))
@router.message(F.text.lower() == "Sorting")
async def sort(message: Message):
    await message.answer(text = ":)", parse_mode = "HTML", reply_markup = algo_sort())

@router.message(Command("Linear"))
@router.message(F.text.lower() == "Linear")
async def line(message: Message):
    await message.answer(text = ":)", parse_mode = "HTML", reply_markup = algo_line())

@router.message(Command("Strings"))
@router.message(F.text.lower() == "Strings")
async def stroki(message: Message):
    await message.answer(text = ":)", parse_mode = "HTML", reply_markup = algo_str())

@router.message(Command("Trees"))
@router.message(F.text.lower() == "Trees")
async def tree(message: Message):
    await message.answer(text = ":(", parse_mode = "HTML", reply_markup = algo_tree())

@router.message(Command("Bin_search"))
@router.message(F.text.lower() == "Bin_search")
async def send_bins(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("bins.txt", "r", encoding="utf-8") as file:
            content = file.read()

        # Отправляем текст пользователю
        await message.answer(content)
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")