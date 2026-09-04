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
            [KeyboardButton(text = '/Strings'), KeyboardButton(text = '/Trees'), KeyboardButton(text = '/Random_and_try')]
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

def algo_random():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='/Algorithms')],
            [KeyboardButton(text = '/Random'), KeyboardButton(text = '/Try')]
        ],
        resize_keyboard = True
    )
    return keyboard

def algo_line():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='/Algorithms')],
            [KeyboardButton(text = '/Bin_search')], [KeyboardButton(text = '/Math')],
            [KeyboardButton(text ='/Struct_and_class')]
            ],
            resize_keyboard = True)
    return keyboard

def algo_str():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text='/Algorithms')],
            [KeyboardButton(text = '/Window'), KeyboardButton(text = '/INF_input')],
            [KeyboardButton(text = '/File_input')], [KeyboardButton(text = '/File_output')],
            [KeyboardButton(text='/Default_functions')]
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

@router.message(Command("Random_and_try"))
@router.message(F.text.lower() == "Random_and_try")
async def sort(message: Message):
    await message.answer(text = ":)", parse_mode = "HTML", reply_markup = algo_random())

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
            bt = file.read()

        # Отправляем текст пользователю
        await message.answer(bt, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("Murge_sort"))
@router.message(F.text.lower() == "Murge_sort")
async def send_bins2(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("ms.txt", "r", encoding="utf-8") as file:
            mst = file.read()

        # Отправляем текст пользователю
        await message.answer(mst, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("Quick_sort"))
@router.message(F.text.lower() == "Quick_sort")
async def send_bins3(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("qs.txt", "r", encoding="utf-8") as file:
            qst = file.read()

        # Отправляем текст пользователю
        await message.answer(qst, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("Window"))
@router.message(F.text.lower() == "Window")
async def send_bins4(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("window.txt", "r", encoding="utf-8") as file:
            wt = file.read()

        # Отправляем текст пользователю
        await message.answer(wt, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("INF_input"))
@router.message(F.text.lower() == "INF_input")
async def send_bins5(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("infi.txt", "r", encoding="utf-8") as file:
            iit = file.read()

        # Отправляем текст пользователю
        await message.answer(iit, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("Default_functions"))
@router.message(F.text.lower() == "Default_functions")
async def send_bins6(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("deff.txt", "r", encoding="utf-8") as file:
            dft = file.read()

        # Отправляем текст пользователю
        await message.answer(dft, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("DFS"))
@router.message(F.text.lower() == "DFS")
async def send_bins7(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("dfs.txt", "r", encoding="utf-8") as file:
            dfst = file.read()

        # Отправляем текст пользователю
        await message.answer(dfst, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("BFS"))
@router.message(F.text.lower() == "BFS")
async def send_bins8(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("bfs.txt", "r", encoding="utf-8") as file:
            bfst = file.read()

        # Отправляем текст пользователю
        await message.answer(bfst, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("DO"))
@router.message(F.text.lower() == "DO")
async def send_bins9(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("do.txt", "r", encoding="utf-8") as file:
            dot = file.read()

        # Отправляем текст пользователю
        await message.answer(dot, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("Dejkstra"))
@router.message(F.text.lower() == "Dejkstra")
async def send_bins10(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("dej.txt", "r", encoding="utf-8") as file:
            dejt = file.read()

        # Отправляем текст пользователю
        await message.answer(dejt, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("Math"))
@router.message(F.text.lower() == "Math")
async def send_bins11(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("cmath.txt", "r", encoding="utf-8") as file:
            mt = file.read()

        # Отправляем текст пользователю
        await message.answer(mt, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("Struct_and_class"))
@router.message(F.text.lower() == "Struct_and_class")
async def send_bins12(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("struct+class.txt", "r", encoding="utf-8") as file:
            sact = file.read()

        # Отправляем текст пользователю
        await message.answer(sact, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("File_input"))
@router.message(F.text.lower() == "File_input")
async def send_bins13(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("fileinput.txt", "r", encoding="utf-8") as file:
            fit = file.read()

        # Отправляем текст пользователю
        await message.answer(fit, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("File_output"))
@router.message(F.text.lower() == "File_output")
async def send_bins14(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("fileoutput.txt", "r", encoding="utf-8") as file:
            fot = file.read()

        # Отправляем текст пользователю
        await message.answer(fot, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()

@router.message(Command("Try"))
@router.message(F.text.lower() == "Try")
async def send_bins15(message: Message):
    try:
        # Читаем файл в кодировке UTF-8
        with open("try.txt", "r", encoding="utf-8") as file:
            tt = file.read()

        # Отправляем текст пользователю
        await message.answer(tt, parse_mode="MarkdownV2")
    except FileNotFoundError:
        await message.answer("Файл с текстом не найден.")
    file.close()