import requests
import os
import sys
script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
os.chdir(script_dir)

# a) Загрузка массива JSON-объектов с сайта jsonplaceholder с использованием requests
url = 'https://jsonplaceholder.typicode.com/posts'  # Пример эндпоинта, возвращает массив объектов
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("JSON-массив успешно загружен. Количество объектов:", len(data))
else:
    print("Ошибка при загрузке:", response.status_code)
    exit()

# b) Создание новой папки 'name' и сохранение индекса (ID) каждого объекта в отдельный файл
folder_name = 'name'
os.makedirs(folder_name, exist_ok=True)  # Создаём папку, если её нет

for item in data:
    index = item['id']  # Беру 'id' как индекс объекта
    file_path = os.path.join(folder_name, f'{index}.txt')
    with open(file_path, 'w') as file:
        file.write(str(index))  # Сохраняем ID в файл

print("Файлы сохранены в папке 'name'.")