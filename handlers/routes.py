from aiogram import Router, F, html
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
            [KeyboardButton(text = '/Algorithms')],
            [KeyboardButton(text = '/Murge_sort'), KeyboardButton(text = '/Quick_sort')]
        ],
        resize_keyboard = True
    )
    return keyboard

def algo_random():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text = '/Algorithms')],
            [KeyboardButton(text = '/Random'), KeyboardButton(text = '/Try')]
        ],
        resize_keyboard = True
    )
    return keyboard

def algo_line():
    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            [KeyboardButton(text = '/Algorithms')],
            [KeyboardButton(text = '/Bin_search')], [KeyboardButton(text = '/Math')],
            [KeyboardButton(text = '/Struct_and_class')]
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
async def send_bins(message: Message):
    with open("bins.txt", "r", encoding="utf-8") as file1:
        bt = file1.read()
        await message.answer(bt)
    with open("binscode.txt", "r", encoding="utf-8") as file1:
        bt = file1.read()
        await message.answer(bt,parse_mode="HTML")
    with open("bins2.txt", "r", encoding="utf-8") as file1:
        bt = file1.read()
        await message.answer(bt)
    with open("bins2code.txt", "r", encoding="utf-8") as file1:
        bt = file1.read()
        await message.answer(bt,parse_mode="HTML")

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
        await message.answer(dft,parse_mode="HTML")

@router.message(Command("DFS"))
async def send_bins7(message: Message):
    with open("dfs.txt", "r", encoding="utf-8") as file7:
        dfst = file7.read()
        await message.answer(dfst)
    with open("dfscode.txt", "r", encoding="utf-8") as file7:
        dfst = file7.read()
        await message.answer(dfst,parse_mode="HTML")
    with open("dfs2.txt", "r", encoding="utf-8") as file7:
        dfst = file7.read()
        await message.answer(dfst)
    with open("dfs2code.txt", "r", encoding="utf-8") as file7:
        dfst = file7.read()
        await message.answer(dfst,parse_mode="HTML")
    with open("dfs3.txt", "r", encoding="utf-8") as file7:
        dfst = file7.read()
        await message.answer(dfst)

@router.message(Command("BFS"))
async def send_bins8(message: Message):
    with open("bfs.txt", "r", encoding="utf-8") as file8:
        bfst = file8.read()
        await message.answer(bfst)
    with open("bfscode.txt", "r", encoding="utf-8") as file8:
        bfs = file8.read()
        await message.answer(bfs, parse_mode="HTML")

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
    with open("cmathcode.txt", "r", encoding="utf-8") as file11:
        mt = file11.read()
        await message.answer(mt,parse_mode="HTML")

@router.message(Command("Struct_and_class"))
async def send_bins12(message: Message):
    with open("struct+class.txt", "r", encoding="utf-8") as file12:
        sact = file12.read()
        await message.answer(sact)
    with open("sccode.txt", "r", encoding="utf-8") as file12:
        sact = file12.read()
        await message.answer(sact,parse_mode="HTML")
    with open("sc2", "r", encoding="utf-8") as file12:
        sact = file12.read()
        await message.answer(sact)
    with open("sc2code", "r", encoding="utf-8") as file12:
        sact = file12.read()
        await message.answer(sact,parse_mode="HTML")
    with open("sc3", "r", encoding="utf-8") as file12:
        sact = file12.read()
        await message.answer(sact)

@router.message(Command("File_input"))
async def send_bins13(message: Message):
    with open("fileinput.txt", "r", encoding="utf-8") as file13:
        fit = file13.read()
        await message.answer(fit)
    with open("FIcode.txt", "r", encoding="utf-8") as file13:
        fit = file13.read()
        await message.answer(fit,parse_mode="HTML")

@router.message(Command("File_output"))
async def send_bins14(message: Message):
    with open("fileoutput.txt", "r", encoding="utf-8") as file14:
        fot = file14.read()
        await message.answer(fot)
    with open("FOcode.txt", "r", encoding="utf-8") as file14:
        fot = file14.read()
        await message.answer(fot,parse_mode="HTML")

@router.message(Command("Try"))
async def send_bins15(message: Message):
    with open("try.txt", "r", encoding="utf-8") as file15:
        tt = file15.read()
        await message.answer(tt)
    with open("trycode.txt", "r", encoding="utf-8") as file15:
        tct = file15.read()
        await message.answer(tct, parse_mode="HTML")