# Проект: Сравнение асинхронного и синхронного чтения файлов

Проект реализует сравнение асинхронного и синхронного подхода к чтению содержимого файлов двоичного формата с добавлением задержки и без неё.

## Установка и требования

Для запуска проекта требуются следующие инструменты:

- **Python**: 3.6 или выше
- **aiofiles**: Для асинхронного чтения

### Установка пакета `aiofiles`

Для работы с асинхронным чтением необходимо предварительно установить пакет `aiofiles`. Сделать это можно c помощью команды:

```bash
pip install aiofiles
```
Для запуска асинхронного и синхронного чтения файла потребуется прописать команды:

`python async_reader.py --directory путь/до/директории/с/файлами/` 

и 

`python sync_reader.py --directory путь/до/директории/с/файлами/` соответственно

---

# Project: Comparing Asynchronous and Synchronous File Reading

The project implements a comparison of asynchronous and synchronous approaches to reading the contents of binary format files, with and without added delay.

## Installation and Requirements

To run the project, the following tools are required:

- **Python**: 3.6 or higher
- **aiofiles**: For asynchronous reading

### Installing the `aiofiles` package

To work with asynchronous reading, you must first install the `aiofiles` package. This can be done using the command:

```bash
pip install aiofiles
```

To execute asynchronous and synchronous file reading, you will need to run the commands:

`python async_reader.py --directory path/to/directory/with/files/`

and

`python sync_reader.py --directory path/to/directory/with/files/` respectively.
