from enum import Enum


class Position:
    column: int
    step: int

    def __init__(self, column: int, step: int):
        self.column = column
        self.step = step


class Character:
    pass


class Cell:
    position: Position
    adjacents: list[Position]
    character: Character

    def __init__(self, position: Position, adjacents: list[Position] = None, character:Character = None):
        self.position = position
        self.adjacents = adjacents
        self.character = character


class StreetSpace:
    pass


class QuaysideSpace:
    pass


class PortSpace:
    pass


class LibertyIsland:
    pass


class LandExit:
    pass


class Tile(Enum):
    pass


class InvestigationTile:
    pass


class AlfredElyBeach:
    pass


class CloudRider:
    pass


class LewisHowardLatimer:
    pass


class MrsEmmaGrant:
    pass


class JamesHCallahan:
    pass


class MonkEastman:
    pass


class FrancisJTumblety:
    pass


class EdwardSmith:
    pass


class Informant:
    pass


class Board:
    pass


class Game:
    pass
