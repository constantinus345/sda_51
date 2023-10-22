import asyncio
from random import randint
async def numarare(a,b):
    print(a)
    timp_asteptare = randint(1,5)
    print(f"Pentru {a} si {b} avem timp de asteptare {timp_asteptare}")
    await asyncio.sleep(2)
    print(b)

async def executare():
    await asyncio.gather(numarare(11,22), numarare(33,44), numarare(55,66), numarare(77,88))

if __name__ == "__main__":
    asyncio.run(executare())
