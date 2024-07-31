from enum import Enum


class LeagueRole(Enum):
    Top = 1
    Jungle = 2
    Mid = 3
    Bot = 4
    Support = 5


class ValorantAgentRole(Enum):
    Controller = 1
    Duelist = 2
    Initiator = 3
    Sentinel = 4


class Map(Enum):
    All = 0
    Bind = 1
    Haven = 2
    Split = 3
    Ascent = 4
    Icebox = 5
    Breeze = 6
    Fracture = 7
    Pearl = 8
    Lotus = 9
    Sunset = 10
    Abyss = 11


class Side(Enum):
    Both = 0
    Attacking = 1
    Defending = 2