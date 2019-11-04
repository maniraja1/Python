from __future__ import annotations

''' parameters with  type '''
def headline(text:str,align:bool = True) -> str:
    ''' Function to fixstring alignment.'''
    '''Note that types are just hints and are suggestive. Python is still dynamically typed language'''

    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f"{text.title()}".center(50,"-")


print(headline('Static Typing'))
print(headline('Static Typing',"center")) ### This will give an error in mypy
print(headline('Static Typing',False))
print(headline.__annotations__) ### This will print the input and output types

''' parameters type as comments. This is for running in older version of python'''
def diamater(radius):
    # type: (float) -> float
    return radius*2

print(diamater.__annotations__)

# headlines.py
def headline2(
    text,           # type: str
    width=80,       # type: int
    fill_char="-",  # type: str
):                  # type: (...) -> str
    return f" {text.title()} ".center(width, fill_char)

print(headline2("type comments work", width=40))


'''Handling collection'''
from typing import Dict, List, Tuple, Sequence,Generator
names: List[str] = ["test","prod","qa"]
version: Tuple[int, int, int] = (3,7,1)
options: Dict[str,int] = {"test": 1, "prod": 0, "qa": 1}


'''Handling Sequence'''
def lowercase(coll: Sequence[str]) -> Generator[str, None, None]:
    for x in coll:
        yield x.lower()
### Passing List
for x in lowercase(["A","B","C"]):
    print(x)
print("--------------------------")

### Passing tuple
for x in lowercase(("A","B","C")):
    print(x)

''' Type Aliasing'''
card = Tuple[str,str]
deck = List[card]

def shuffle_deck() -> Tuple[deck, deck, deck, deck]:
    suit: List[str] = ['s', 'c', 'd', 'h']
    val: List[str] = [str(x) for x in range(1,11)]
    print(val)
    cards: card = ((x1, y) for x1 in suit for y in val)
    #print(*cards)
    decks: deck = [x2 for x2 in cards]

    return (decks[0::4], decks[1::4], decks[2::4], decks[3::4])


for x in shuffle_deck():
    print(x)

'''No return'''
from typing import NoReturn

def empty() -> NoReturn:
    pass

empty()


''' Any'''
from typing import Sequence, Any, List
from collections.abc import Iterable
def squares(coll: Any) -> Sequence[Any]:
    out:List[Any]=list()
    if isinstance(coll,Iterable):
        for x in coll:
            out.append(x*x)
    else:
        out.append(coll*coll)

    return out

print(squares([1,2,3,4])) ### passing list
print(squares(1)) ### passing int



'''Type Variable'''
from typing import TypeVar, Sequence
import random

Choosable= TypeVar("Choosable")

def choose1(items: Sequence[Choosable]) -> Choosable:
    return random.choice(items)

name = [1,2,3,1,1]
choice1 = choose1(name)
print(choice1)

##reveal_type(choice1)
Replacable= TypeVar("Replacable", float, str) ### Here we restrict type to float and str and so even though we pass an int mypy reveals that it is a float

def choose2(items: Sequence[Replacable]) -> Replacable:
    return random.choice(items)


choice2 = choose2(name)
print(choice2)

###reveal_type(choice2)

'''Optional'''

def area1(radius: float, pi: float=None ) -> float:
    if pi is None:
        pi = 3.18
    return pi*radius*radius

print(area1(5,4))

from typing import Optional
def area2(radius: float, pi: Optional[float]=None ) -> float:
    if pi is None:
        pi = 3.18
    return pi*radius*radius

print(area2(5,4))


'''classes as type'''
from typing import Sequence
class Card:
    def __init__(self,suit: str, value: str):
        self.suit=suit
        self.value=value

##from __future__ import annotations
### __future__ is used for forward reference when you reference the class type inside the same class
class Deck:
    def __init__(self, cards: Sequence[Card]):
        self.cards=cards
    def shuffle(self, inpput: Deck):
        pass


'''annotating cls and self'''


'''annotating args and kwargs'''

class Numbers:
    def __init__(self, *args: int) -> None:
        self.sum = 0
        self.args=args

    def add(self):
        for x in self.args:
            self.sum += x
        return self.sum


num = Numbers(1,2,3,4,5,5)
print(num.args)
num.add()
print(num.sum)

