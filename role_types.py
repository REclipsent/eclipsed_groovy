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
