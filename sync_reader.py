import datetime
import time
import os
from argparse import ArgumentParser


def read_file(filename):
    with open(filename, mode='rb') as f:
        print(filename)
        while True:
            time.sleep(0.001)
            data = f.read(1024)
            if not data:
                print(filename, "done ###############")
                break


begin = datetime.datetime.now()
parser = ArgumentParser()
parser.add_argument('--directory', required=True, help='Путь к директории с файлами')
args = parser.parse_args()
files = [os.path.join(root, file) for root, dirs, files in os.walk(args.directory) for file in files if file.endswith('.bin')]
if not os.path.exists(args.directory):
    print(f"Директория '{args.directory}' не найдена.")
else:
    for f in files:
        read_file(f)

    print(datetime.datetime.now() - begin)
