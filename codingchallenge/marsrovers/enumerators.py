from enum import Enum


class Instructions(Enum):
    L = "L"
    Left = "L"
    R = "R"
    Right = "R"
    M = "M"
    Move = "M"


class Directions(Enum):
    N = "N"
    North = "N"
    E = "E"
    East = "E"
    S = "S"
    South = "S"
    W = "W"
    West = "W"
