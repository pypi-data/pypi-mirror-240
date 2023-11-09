import os
from typing import Optional


def recur(path: str, include: Optional[list] = None) -> list[str]:
    """
    Поиск файлов во всех папках
    :param path: Путь до папки
    :param include: Искать файлы с определенным расширением ['.jpg', '.exe'...]
    :return: list[str]
    """
    result = []
    include = tuple(include) if include else ()
    for curdir, _, files in os.walk(path):
        for file in files:
            if not include or file.lower().endswith(include):
                result.append(os.path.join(curdir, file))
    return result


if __name__ == '__main__':
    from pprint import pprint

    _dirpath = r"i:\spamchik\scripts"
    _res = recur(_dirpath)
    pprint(_res)
