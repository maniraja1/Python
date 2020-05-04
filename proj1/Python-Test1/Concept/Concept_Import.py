
'''
from morsels_smoosh import *
    If you need  functions to be listed by dir()  add functions to __all__
    __all__ = [f'sm{"o" * i}sh' for i in range(2, 11)]



import morsels_smoosh as x
    If you need  functions to be listed by  print(dir(x)) add function to __dir__

    __all__ = [f'sm{"o" * i}sh' for i in range(2, 11)]
    def __dir__():
        return __all__


'''