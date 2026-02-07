import aiohttp
import asyncio
import os
import json

async def main():
    # a) Асинхронная загрузка JSON с aiohttp
    url = 'https://jsonplaceholder.typicode.com/posts'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                print("JSON-массив успешно загружен асинхронно. Количество объектов:", len(data))
            else:
                print("Ошибка при загрузке:", response.status)
                return

    # b) Создание папки и сохранение ID
    folder_name = 'name_async'
    os.makedirs(folder_name, exist_ok=True)

    for item in data:
        index = item['id']
        file_path = os.path.join(folder_name, f'{index}.txt')
        with open(file_path, 'w') as file:
            file.write(str(index))

    print("Файлы сохранены в папке 'name_async'.")

# Запуск асинхронного кода
asyncio.run(main())