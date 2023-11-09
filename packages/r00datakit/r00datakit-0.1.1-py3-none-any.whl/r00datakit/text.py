import re


class TextUtil:
    def __init__(self, text: str):
        self._text = text

    def __str__(self):
        return self._text

    def __repr__(self):
        return self._text

    def __len__(self):
        return len(self._text)

    @property
    def this_ip(self):
        p = re.compile(r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
                       r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
                       r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\."
                       r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$")
        return True if p.match(self._text) else False


if __name__ == '__main__':
    _text = TextUtil("244.0.244.244")
    print(_text.this_ip)
