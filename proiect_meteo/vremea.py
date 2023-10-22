# import the module
import python_weather
import asyncio
import os


async def getweather(oras):
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast from a city
        weather = await client.get(oras)

        # returns the current day's forecast temperature (int)
        return weather.current.temperature



# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
if __name__ == "__main__":
    #Codul se va executa doar daca acest fisier este rulat direct, nu si la import in alte fisiere
    localitate = "Arieseni, Alba"
    tempx = asyncio.run(getweather(localitate))
    print(f"Temp in {localitate} este {tempx} Celsius")
