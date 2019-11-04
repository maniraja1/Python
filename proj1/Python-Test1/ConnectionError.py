from abc import ABCMeta

class Text(metaclass=ABCMeta):
    def __init__(self):
        self._val = 1

Text.register(str)

print(issubclass(str, Text))
