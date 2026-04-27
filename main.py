import asyncio
import logging
from aiogram.types import Message
from aiogram import Bot,Dispatcher,F
from aiogram.filters import Command
from dotenv import load_dotenv
import os
load_dotenv()
import wikipedia
wikipedia.set_lang("uz")
API_TOKEN=os.getenv("API_TOKEN")
bot=Bot(token=API_TOKEN)
dp=Dispatcher()
@dp.message(Command('start'))
async def start_cmd(message:Message):
    await message.reply(f"""
 Assalomu alaykum {message.from_user.full_name}
 wikepidia botimizga xush kelibsiz so'z yozing men ma'lumot qidiraman
 """)
@dp.message(F.text)
async def translator_bot(message:Message):
    try:
        text=message.text
        wikepidia=wikipedia.summary(text,sentences=5)
        await message.answer(f"wikepedidan javob: \n\n {wikepidia}")
    except Exception as error:
        await message.answer(f"Botda xatolik {error}")

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())