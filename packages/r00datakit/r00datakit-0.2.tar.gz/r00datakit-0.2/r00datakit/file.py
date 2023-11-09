import mmap
from pathlib import Path

from r00log.logger import log


class FileUtil:
    def __init__(self, filepath: str):
        self._filepath = filepath
        self._name = Path(filepath).name

    def __str__(self):
        return f'{self._name}'

    def __repr__(self):
        return f'{self._name}'

    def __len__(self):
        return self.count_lines()

    def __iter__(self):
        with open(self._filepath) as f:
            for line in f:
                yield line.strip()

    def count_lines(self) -> int:
        """
        Подсчет количества строк в файле
        @return: int
        """
        with open(self._filepath, 'r') as f:
            mmapped_file = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
            result = bytes(mmapped_file).count(b'\n')
        log.trace(f'file {self._name}: {result} count lines')
        return result

    def get_filesize(self) -> int:
        """
        Возвращает размер файла в килобайтах
        @return: int
        """
        file_kbyte = int(Path(self._filepath).stat().st_size)
        log.trace(f'FileUtil size {self._name}: {file_kbyte} kbyte')
        return file_kbyte

    def load(self, lines=True) -> str | list:
        """
        Возвращает данные файла целиком.
        @param lines: разбить данные по строкам
        """
        with open(self._filepath) as f:
            return f.read().splitlines() if lines else f.read()


if __name__ == '__main__':
    #_filepath = r"G:\project\Snapchat\Base\snapchat.all.mix.txt"
    _filepath = r"G:\project\Snapchat\Base\snapchat.all.au.txt"
    _file = FileUtil(_filepath)

    # _file.count_lines()
    # _file.get_filesize()
    # _file.load(lines=False)
