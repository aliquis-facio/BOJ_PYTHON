from datetime import datetime
from os import scandir


def convert_date(timestamp):
    d = datetime.fromtimestamp(timestamp)
    formated_date = d.strftime('%Y-%m-%d, %H:%M:%S')
    return formated_date


def get_files():
    dir_entries = scandir('test_dir')
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            print(f'{entry.name}\t 최종 수정: {convert_date(info.st_mtime)}')


get_files()
