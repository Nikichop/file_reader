# Содержимое для каждого файла
сontents = [
    "Вывод из 1 файла",
    "Здесь данные из файла номер два",
    "Третий файл содержит этот текст",
    "Четвертый файл заполнен этой строкой",
    "Пятый файл и его уникальные данные",
    "Шестой файл отличается этими словами",
    "Седьмой файл и его индивидуальный текст",
    "Восьмой файл заканчивается здесь"
]

for i, content in enumerate(сontents, start=1):
    file_name = f"file{i}.bin"
    with open(file_name, 'wb') as f:
        f.write(content.encode())

print("Файлы успешно созданы")
