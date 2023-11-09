from dataclasses import dataclass as __dataclass
from typing import TypeAlias as __TypeAlias

AtomicValue: __TypeAlias = int|float|str|bool
SimpleValue: __TypeAlias = AtomicValue|tuple[AtomicValue,AtomicValue]

@__dataclass
class Block(object):
    A: list[SimpleValue]
    B: str|None
    C: list['Block']|None

