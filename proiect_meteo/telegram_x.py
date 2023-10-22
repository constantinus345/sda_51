from vremea import getweather
import asyncio
#https://github.com/python-telegram-bot/python-telegram-bot
#pip install python-telegram-bot
#!!! Uneori libraria are denumiri diferite intre pip install si import!
import telegram

from super_secret import cod_telegram_bot, id_constantin

# localitate = "Oslo"
# tempx = asyncio.run(getweather(localitate))
# print(f"Temp in {localitate} este {tempx} Celsius")

#pentru a crea un bot, vorbesc pe telegram cu @BotFather
async def telegram_trimite_mesaj(chat_idx, text_x):
    bot = telegram.Bot(cod_telegram_bot)
    async with bot:
        await bot.send_message(text=text_x, chat_id=chat_idx)

#pentru a afla id-ul tau, foloseste chatul cu RawDataBot

async def executare_mesaj_telegram(text_trimis, id_trimis):
    await telegram_trimite_mesaj(chat_idx=id_trimis, text_x= text_trimis)

if __name__ == "__main__":
    asyncio.run(executare_mesaj_telegram())