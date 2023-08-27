import asyncio

from vremea import getweather
from telegram_x import executare_mesaj_telegram
from openai_stuff import text_imbracaminte
from super_secret import id_constantin

if __name__ == "__main__":
    localitatea = "Sibiu, Romania"
    temperatura_afara = asyncio.run(getweather(localitatea))
    print(f"Temperatura in {localitatea} este {temperatura_afara} grade Celsius")

    text_custom = text_imbracaminte(temperatura_afara)
    print(text_custom)
    asyncio.run(executare_mesaj_telegram(text_trimis = text_custom, id_trimis= id_constantin))
