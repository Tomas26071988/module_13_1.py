import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):               #цикл для поднятия 5 шаров.
        await asyncio.sleep(1/power)   # сделал обратно пропорциональ - это чтобы у кого сила больше тот и победит
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    tasks = [
        asyncio.create_task(start_strongman('Artem',100)),
        asyncio.create_task(start_strongman('Arseny',70)),
        asyncio.create_task(start_strongman('Masha',30))
    ]
    await asyncio.gather(*tasks)

asyncio.run(start_tournament())
