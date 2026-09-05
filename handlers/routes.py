from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)

router = Router()

def get_main_reply_keyboard():
    buttons = [
        [InlineKeyboardButton(text = "Алгоритмы", callback_data="Algorithms")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_main_reply_algo():
    buttons = [
        [InlineKeyboardButton(text = 'Сортировки', callback_data="Sorting"), InlineKeyboardButton(text = 'Линейные', callback_data= "Linear")],
        [InlineKeyboardButton(text = 'Строки', callback_data="Strings"), InlineKeyboardButton(text = 'Деревья', callback_data="Trees"), InlineKeyboardButton(text = 'Random и try', callback_data="Random_and_try")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def algo_sort():
    buttons = [
        [InlineKeyboardButton(text='Алгоритмы', callback_data="Algorithms")],
        [InlineKeyboardButton(text = 'Murge_sort', callback_data="Murge_sort"), InlineKeyboardButton(text = 'Quick_sort',callback_data="Quick_sort")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def algo_random():
    buttons = [
        [InlineKeyboardButton(text = 'Алгоритмы', callback_data="Algorithms")],
        [InlineKeyboardButton(text = 'Random', callback_data="Random"), InlineKeyboardButton(text = '/Try', callback_data="Try")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def algo_line():
    buttons = [
        [InlineKeyboardButton(text='Алгоритмы',callback_data="Algorithms")],
        [InlineKeyboardButton(text = 'Бин поиск',callback_data="Bin_search")], [InlineKeyboardButton(text = 'Math',callback_data="Math")],
        [InlineKeyboardButton(text ='Struct и class',callback_data="Struct_and_class")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def algo_str():
    buttons = [
        [InlineKeyboardButton(text='Алгоритмы',callback_data="Algorithms")],
        [InlineKeyboardButton(text ='Окно',callback_data="Window"), InlineKeyboardButton(text = 'INF input',callback_data="INF_input")],
        [InlineKeyboardButton(text ='File input',callback_data="File_input")], [InlineKeyboardButton(text = 'File output',callback_data="File_output")],
        [InlineKeyboardButton(text='Default функции',callback_data="Default_functions")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def algo_tree():
    buttons = [
        [InlineKeyboardButton(text='Алгоритмы',callback_data="Algorithms")],
        [InlineKeyboardButton(text = 'DFS',callback_data="DFS"), InlineKeyboardButton(text = 'BFS',callback_data="BFS")],
        [InlineKeyboardButton(text = 'Дейкстра',callback_data="Dejkstra"), InlineKeyboardButton(text = 'ДО',callback_data="DO")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

@router.message(F.text == "/start")
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}. Мы команда вайбкодеров, которая хочет пройти на ICPC", parse_mode = "HTML", reply_markup = get_main_reply_keyboard())

@router.callback_query(F.data == "Algorithms")
async def algo(callback: CallbackQuery):
    await callback.message.answer(text = ";)", parse_mode = "HTML", reply_markup = get_main_reply_algo())

@router.callback_query(F.data == "Sorting")
async def sort(callback: CallbackQuery):
    await callback.message.answer(text = ":)", parse_mode = "HTML", reply_markup = algo_sort())

@router.callback_query(F.data == "Random_and_try")
async def rat(callback: CallbackQuery):
    await callback.message.answer(text = ":)", parse_mode = "HTML", reply_markup = algo_random())

@router.callback_query(F.data == "Linear")
async def line(callback: CallbackQuery):
    await callback.message.answer(text = ":)", parse_mode = "HTML", reply_markup = algo_line())

@router.callback_query(F.data == "Strings")
async def stroki(callback: CallbackQuery):
    await callback.message.answer(text = ":)", parse_mode = "HTML", reply_markup = algo_str())

@router.callback_query(F.data == "Trees")
async def tree(callback: CallbackQuery):
    await callback.message.answer(text = ":(", parse_mode = "HTML", reply_markup = algo_tree())

@router.callback_query(F.data == "Bin_search")
async def send_bins(callback:CallbackQuery):
    with open("bins.txt", "r", encoding="utf-8") as file1:
        bt = file1.read()
        await callback.message.answer(bt)

@router.message(Command("Murge_sort"))
async def send_bins2(message: Message):
    with open("ms.txt", "r", encoding="utf-8") as file2:
        mst = file2.read()
        await message.answer(mst)

@router.message(Command("Quick_sort"))
async def send_bins3(message: Message):
    with open("qs.txt", "r", encoding="utf-8") as file3:
        qst = file3.read()
        await message.answer(qst)

@router.message(Command("Window"))
async def send_bins4(message: Message):
    with open("window.txt", "r", encoding="utf-8") as file4:
        wt = file4.read()
        await message.answer(wt)

@router.message(Command("INF_input"))
@router.message(F.text.lower() == "INF_input")
async def send_bins5(message: Message):
    with open("infi.txt", "r", encoding="utf-8") as file5:
        iit = file5.read()
        await message.answer(iit)

@router.message(Command("Default_functions"))
async def send_bins6(message: Message):
    with open("deff.txt", "r", encoding="utf-8") as file6:
        dft = file6.read()
        await message.answer(dft)

@router.message(Command("DFS"))
async def send_bins7(message: Message):
    with open("dfs.txt", "r", encoding="utf-8") as file7:
        dfst = file7.read()
        await message.answer(dfst)
@router.message(Command("BFS"))
async def send_bins8(message: Message):
    with open("bfs.txt", "r", encoding="utf-8") as file8:
        bfst = file8.read()
        await message.answer(bfst)

@router.message(Command("DO"))
async def send_bins9(message: Message):
    with open("do.txt", "r", encoding="utf-8") as file9:
        dot = file9.read()
        await message.answer(dot)

@router.message(Command("Dejkstra"))
async def send_bins10(message: Message):
    with open("dej.txt", "r", encoding="utf-8") as file10:
        dejt = file10.read()
        await message.answer(dejt)

@router.message(Command("Math"))
async def send_bins11(message: Message):
    with open("cmath.txt", "r", encoding="utf-8") as file11:
        mt = file11.read()
        await message.answer(mt)

@router.message(Command("Struct_and_class"))
async def send_bins12(message: Message):
    with open("struct+class.txt", "r", encoding="utf-8") as file12:
        sact = file12.read()
        await message.answer(sact)

@router.message(Command("File_input"))
async def send_bins13(message: Message):
    with open("fileinput.txt", "r", encoding="utf-8") as file13:
        fit = file13.read()
        await message.answer(fit)

@router.message(Command("File_output"))
async def send_bins14(message: Message):
    with open("fileoutput.txt", "r", encoding="utf-8") as file14:
        fot = file14.read()
        await message.answer(fot)

@router.message(Command("Try"))
async def send_bins15(message: Message):
    with open("try.txt", "r", encoding="utf-8") as file15:
        tt = file15.read()
        await message.answer(tt)