import argparse
import datetime
import asyncio
import aiofiles
import os


async def read_file(filename):
    async with aiofiles.open(filename, mode='rb') as f:
        print(filename)
        while True:
            await asyncio.sleep(0.001)
            data = await f.read(1024)
            if not data:
                print(filename, "done ###############")
                break


async def main():
    begin = datetime.datetime.now()
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', required=True, help='Путь к директории с файлами')
    args = parser.parse_args()
    files = [os.path.join(root, file) for root, dirs, files in os.walk(args.directory) for file in files if file.endswith('')]
    if not os.path.exists(args.directory):
        print(f"Директория '{args.directory}' не найдена.")
    else:
        tasks = [read_file(f) for f in files]
        for future in asyncio.as_completed(tasks):
            await future

        print(datetime.datetime.now() - begin)

if __name__ == '__main__':
    asyncio.run(main())