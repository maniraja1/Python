'''
A data class is a class typically containing mainly data, although there aren’t really any restrictions.
It is created using the new @dataclass decorator.

A data class comes with basic functionality already implemented. For instance, you can instantiate, print(__repr__),
and compare
data class instances straight out of the box

The @dataclass decorator has two forms. So far you have seen the simple form where @dataclass is specified without
any parentheses and parameters. However, you can also give parameters to the @dataclass() decorator in parentheses.
The following parameters are supported:
init: Add .__init__() method? (Default is True.)
repr: Add .__repr__() method? (Default is True.)
eq: Add .__eq__() method? (Default is True.)
order: Add ordering methods? (Default is False.)
unsafe_hash: Force the addition of a .__hash__() method? (Default is False.)
frozen: If True, assigning to fields raise an exception. (Default is False.)
Notes:
        Introduced in python 3.7
    Defaults
        You can provide default values to fields
        Fields that does not have defaults cannot follow that has defaults
    Type hinting
        Type hinting only does not enforce
    field
        The field() specifier is used to customize each field of a data class individually.
        default: Default value of the field
        default_factory: Function that returns the initial value of the field
        init: Use field in .__init__() method? (Default is True.)
        repr: Use field in repr of the object? (Default is True.)
        compare: Include the field in comparisons? (Default is True.)
        hash: Include the field when calculating hash()? (Default is to use the same as for compare.)
        metadata: A mapping with information about the field
        Order=True
    Frozen=True
        If set to true then attributes cannot be modified
        However if the attribute references a mutable object then this does not hold true
    __post_init__
        Used when you need define an attribute based off of other attributes
    inheritance
        data class can be inherited however if the data class has default attributes and the child class does not
        this will throw an error
    __slots__
        You can use slots with data class for faster performance however attributes cannot have default values


    iterator yield astuple
'''

from dataclasses import dataclass, field
from typing import List

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

pos1 = Position('sfo')
print(pos1)


'''Example 2'''
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

@dataclass(order=True)
class PlayingCard:
    rank: str
    suit: str
    sort_index: int = field(init=False, repr=False)

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        return f'{self.suit}{self.rank}'

@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str

@dataclass(frozen=True)
class ImmutableDeck:
    cards: List[PlayingCard]


queen_of_hearts = ImmutableCard('Q', '♡')
ace_of_spades = ImmutableCard('A', '♠')
queen_of_hearts2 = PlayingCard('Q', '♡')
ace_of_spades2 = PlayingCard('A', '♠')

deck = ImmutableDeck([queen_of_hearts, ace_of_spades])
deck2 = ImmutableDeck([queen_of_hearts2, ace_of_spades2])

print(deck)
print(deck2)

