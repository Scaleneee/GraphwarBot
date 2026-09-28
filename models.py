from dataclasses import dataclass

# coordinates
@dataclass
class Point:
    x: float
    y: float

@dataclass
class Soldier:
    position: Point
    # default: false
    is_enemy: bool = False